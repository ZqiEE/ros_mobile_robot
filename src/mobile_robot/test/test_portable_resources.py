from pathlib import Path
import os
import runpy
from unittest.mock import patch


PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def test_world_uses_named_model_resource():
    world = (PACKAGE_ROOT / 'sdf' / 'warehouse.sdf').read_text()
    assert '<uri>model://finalassembly_v3</uri>' in world
    assert 'file:///home/' not in world


def test_launch_registers_installed_sdf_resource_path():
    launch = (PACKAGE_ROOT / 'launch' / 'bringup.launch.py').read_text()
    assert 'IGN_GAZEBO_RESOURCE_PATH' in launch
    assert 'PathJoinSubstitution([pkg_share, "models"])' in launch


def test_setup_installs_a_named_model_directory():
    previous = Path.cwd()
    captured = {}
    try:
        os.chdir(PACKAGE_ROOT)
        with patch('setuptools.setup', side_effect=lambda **kwargs: captured.update(kwargs)):
            runpy.run_path(str(PACKAGE_ROOT / 'setup.py'), run_name='__main__')
    finally:
        os.chdir(previous)
    installed = {
        (destination.replace('\\', '/'), Path(source).name)
        for destination, sources in captured['data_files']
        for source in sources
    }
    model_root = 'share/mobile_robot/models/finalassembly_v3'
    assert (model_root, 'model.config') in installed
    assert (model_root, 'model.sdf') in installed
    assert (model_root + '/meshes/base_link_1', 'body1_visual.obj') in installed

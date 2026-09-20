from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def test_world_uses_named_model_resource():
    world = (PACKAGE_ROOT / 'sdf' / 'warehouse.sdf').read_text()
    assert '<uri>model://finalassembly_v3</uri>' in world
    assert 'file:///home/' not in world


def test_launch_registers_installed_sdf_resource_path():
    launch = (PACKAGE_ROOT / 'launch' / 'bringup.launch.py').read_text()
    assert 'IGN_GAZEBO_RESOURCE_PATH' in launch
    assert 'PathJoinSubstitution([pkg_share, "sdf"])' in launch

import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'mobile_robot'


def package_files(data_files, directory, install_directory=None):
    """Recursively add files preserving folder structure"""
    for root, _, files in os.walk(directory):
        relative_root = os.path.relpath(root, directory)
        install_path = os.path.join(
            'share', package_name, install_directory or directory)
        if relative_root != '.':
            install_path = os.path.join(install_path, relative_root)
        file_paths = [os.path.join(root, f) for f in files]

        if file_paths:
            data_files.append((install_path, file_paths))

    return data_files


data_files = [
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),

    ('share/' + package_name, ['package.xml']),

    (os.path.join('share', package_name, 'launch'),
        glob('launch/*.py')),

    (os.path.join('share', package_name, 'config'),
        glob('config/*')),
]

data_files = package_files(data_files, 'sdf')
data_files = package_files(
    data_files, 'sdf', os.path.join('models', 'finalassembly_v3'))


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ishan',
    maintainer_email='ishansingla.zy@gmail.com',
    description='Mobile robot package',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'state_publisher = mobile_robot.state_publisher:main',
        ],
    },
)

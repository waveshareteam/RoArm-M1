from setuptools import setup

package_name = 'serial_ctrl'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='roarm',
    maintainer_email='roarm@todo.todo',
    description='Serial ctrl',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'serial_ctrl = serial_ctrl.serial_ctrl_py:main'
        ],
    },
)

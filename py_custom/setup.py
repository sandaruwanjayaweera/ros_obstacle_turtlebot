from setuptools import setup

package_name = 'py_custom'

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
    maintainer='san',
    maintainer_email='sandaruwan.jayaweera@oulu.fi',
    description='CAM information broadcasting using ROS2',
    license='TODO: License declaration',
    tests_require=['pytest'],
entry_points={
        'console_scripts': [
                'talker = py_custom.publisher_member_function:main',
                'listener = py_custom.subscriber_member_function:main',
                'talker_cw = py_custom.pub_denm_cw:main',
                'listener_cw = py_custom.sub_denm_cw:main',
        ],
},
)

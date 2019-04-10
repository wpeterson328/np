from setuptools import find_packages, setup

install_requires = [
    'requests',
]


setup(
    name='np',
    version="0.1",
    author="wyatt peterson",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    include_package_data=True,
    license='Other/Proprietary License',
    description="Neptune's Paranoia",
    url='https://github.com/wpeterson328/np',
    entry_points={
        'console_scripts': [
            'np = np:main'
        ]
    },
)

from setuptools import setup, find_packages

setup(
    name='text_beginner',
    version='0.1',
    description='Log Processing Application',
    author='Your Name',
    author_email='Your Email',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'logscan = logscan.cmd:main' 
        ]
    }, 
)

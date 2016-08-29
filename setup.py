from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
setup(
    name='gbdx-task-interface',
    version='0.0.2',
    packages=find_packages(),
    description='A helper base class for easier GBDX application on-boarding.',
    url='https://github.com/tdg-platform',
    author='GBDX (Dmitry Zviagintsev)',
    author_email='dmitry.zviagintsev@digitialglobe.com',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
        package_data={
        'gbdx_task_interface': [],
    },
)

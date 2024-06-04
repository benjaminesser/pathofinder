import os
from setuptools import setup, find_packages

setup(
    name='snpfinder',
    version='1.0',
    description='Command-line script to perform variant calling of mpileup files',
    author='Benjamin Esser and Ehsun Yazdani',
    author_email='besser@ucsd.edu and eyazdani@ucsd.edu',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snpfinder=snpfinder.snpfinder:main"
        ],
    },
)

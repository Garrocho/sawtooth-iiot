import os
import subprocess

from setuptools import setup, find_packages

data_files = []

setup(
    name='iiot-cli',
    version='1.0',
    description='Sawtooth IIoT Example',
    author='Garrocho',
    url='https://github.com/garrocho/sawtooth-iiot',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'colorlog',
        'protobuf',
        'sawtooth-sdk',
        'sawtooth-signing',
        'PyYAML',
    ],
    data_files=data_files,
    entry_points={
        'console_scripts': [
            'iiot = iiot_app:main',
        ]
    })
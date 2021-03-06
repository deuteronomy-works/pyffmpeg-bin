# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', 'r') as rm:
    long_desc = rm.read()

setup(
    name='pyffmpeg-bin',
    version='1.8.0.1',
    package_data={
        '': ['static/bin/*/ffmpeg', 'static/bin/windows/ffmpeg.exe']
    },
    description='FFmpeg wrapper for python',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/deuteronomy-works/pyffmpeg-bin',
    author='Amoh - Gyebi Godwin Ampofo Michael',
    author_email='amohgyebigodwin@gmail.com',
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords='ffmpeg, FFmpeg, audio, pyffmpeg',
    packages=find_packages(),
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import stoqs_permalink
version = stoqs_permalink.__version__

setup(
    name='stoqs_permalink',
    version=version,
    author="Mike McCann",
    author_email='MBARIMike@gmail.com',
    packages=[
        'stoqs_permalink',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['stoqs_permalink/manage.py'],
)

#!/usr/bin/env python

from setuptools import setup

setup(
    name="bugs-chart.py",
    version="1.0.0",
    description="Python API for downloading Bugs charts",
    author="Lou Park",
    author_email="gold24park@gmail.com",
    url="https://github.com/gold24park/bugs-chart",
    py_modules=["bugs"],
    license="MIT License",
    install_requires=["requests >= 2.28.2"],
)

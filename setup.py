#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bugs-chart.py",
    version="1.0.4",
    description="Python API for downloading Bugs charts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lou Park",
    author_email="gold24park@gmail.com",
    url="https://github.com/gold24park/bugs-chart.py",
    py_modules=["bugs"],
    license="MIT License",
    install_requires=["requests >= 2.28.2"],
)

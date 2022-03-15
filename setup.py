# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "codingtask2"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
]

setup(
    name=NAME,
    version=VERSION,
    description="codingtask2 merge module",
    author_email="",
    author="Markus Sattler",
    url="",
    keywords=["", "codingtask2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': []},
    include_package_data=True,
    entry_points={},
    long_description="""\
    coding task 2
    """
)


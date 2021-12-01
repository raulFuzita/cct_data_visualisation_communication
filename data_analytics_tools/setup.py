#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils.util import convert_path

setup(name='DataAnalyticsTools',
      version=__version__,
      description='Python Distribution Utilities for Data Analytics',
      author='Raul Macedo Fuzita',
      author_email='raul.fuzita@gmail.com',
      packages=['data_analytics_tools'],
      package_dir={'data_analytics_tools': 'src/data_analytics_tools'}
)

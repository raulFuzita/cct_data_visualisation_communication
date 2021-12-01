#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('src/data_analytics_tools/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(name='DataAnalyticsTools',
      version=main_ns['__version__'],
      description='Python Distribution Utilities for Data Analytics',
      author='Raul Macedo Fuzita',
      author_email='raul.fuzita@gmail.com',
      packages=['data_analytics_tools'],
      package_dir={'data_analytics_tools': 'src/data_analytics_tools'}
)

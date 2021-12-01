#!/usr/bin/env python

from distutils.core import setup

setup(name='DataAnalyticsTools',
      version='1.0',
      description='Python Distribution Utilities for Data Analytics',
      author='Raul Macedo Fuzita',
      author_email='raul.fuzita@gmail.com',
      packages=['data_analytics'],
      package_dir={'data_analytics': 'src/data_analytics'}
)

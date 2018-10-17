#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='lofty-django-helpers',
      version='0.0.1',
      description='Lofty\'s favorite Django helper methods and modules.',
      author='Lofty Labs',
      author_email='hello@hirelofty.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=['django-storages>=1.7.1', 'boto3>=1.9.25'],
      license='LICENSE',
    )
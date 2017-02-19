# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from cmsplugin_gridloading import __version__


setup(
    name='CMS Plugin Gridloading',
    version=__version__,
    description=open('README.rst').read(),
    author='Mathieu Meylan',
    author_email='m.meylan@gmail.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)

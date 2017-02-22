#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from cmsplugin_gridloading import __version__

REQUIREMENTS = [
    'django-cms>=3.3.1',
    'django-filer>=1.2.4',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='djangocms-gridloading',
    version=__version__,
    url='https://github.com/matinfo/plugincms-gridloading',
    license='MIT',
    author='Mathieu Meylan',
    author_email='m.meylan@gmail.com',
    description=('Grid loading plugin to django CMS.'),
    long_description=open('README.rst').read(),
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
)

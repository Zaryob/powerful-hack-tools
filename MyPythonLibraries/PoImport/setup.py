#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
poimport setup script.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import poimport

desc = 'A library to load and create po translation files.'

if __name__ == '__main__':
    setup(name="poimport",
          version=1.01,
          description='A library to load and create po translation files.',
          long_description='A library to load and create po translation files.',
          license="GNU AGPLv3",
          author="Süleyman Poyraz (Zaryob)",
          author_email="zaryob.dev@gmail.com",
          maintainer="Zaryob",
          maintainer_email="zaryob.dev@gmail.com",
          url="https://github.com/Zaryob/powerful-hack-tools",
          platforms=['posix'],
          classifiers = [
                        'Environment :: Console',
                        'Environment :: Web Environment',
                        'Intended Audience :: Developers',
                        'Intended Audience :: System Administrators',
                        'License :: OSI Approved :: MIT License',
                        'Operating System :: OS Independent',
                        'Programming Language :: Python',
                        'Programming Language :: Python :: 2',
                        'Programming Language :: Python :: 2.5',
                        'Programming Language :: Python :: 2.6',
                        'Programming Language :: Python :: 2.7',
                        'Programming Language :: Python :: 3',
                        'Programming Language :: Python :: 3.0',
                        'Programming Language :: Python :: 3.1',
                        'Programming Language :: Python :: 3.2',
                        'Programming Language :: Python :: 3.3',
                        'Programming Language :: Python :: 3.4',
                        'Programming Language :: Python :: 3.5',
                        'Programming Language :: Python :: 3.6',
                        'Programming Language :: Python :: Implementation :: PyPy',
                        'Topic :: Software Development :: Libraries :: Python Modules',
                        'Topic :: Software Development :: Internationalization',
                        'Topic :: Software Development :: Localization'
          ],
          py_modules=['poimport']
    )


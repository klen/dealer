#!/usr/bin/env python

"""
Dealer
------

SCM watcher tool. Get current revision and send update notify.

"""

import os
import sys

from setuptools import setup, find_packages

from dealer import __version__, __project__, __license__


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

install_requires = ['gitpython>=0.2']
if sys.version_info < (2, 7):
    install_requires.append('importlib')


META_DATA = dict(
    name=__project__,
    version=__version__,
    license=__license__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    platforms=('Any'),

    author='Kirill Klenov',
    author_email='horneds@gmail.com',
    url=' http://github.com/klen/Flask-Mixer',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

    packages=find_packages(),
    install_requires=install_requires,
    tests_require=('unittest2', 'flask'),
    test_suite = 'tests',
)


if __name__ == "__main__":
    setup(**META_DATA)

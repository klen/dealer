#!/usr/bin/env python

"""
Dealer
------

SCM watcher tool. Get current revision and send update notify.

"""

import sys
from os import path as op

from setuptools import setup


def read(fname):
    try:
        return open(op.join(op.dirname(__file__), fname)).read()
    except IOError:
        return ''


NAME = 'dealer'

CURDIR = op.dirname(__file__)
MODULE = __import__(NAME)
README = op.join(CURDIR, 'README.rst')
REQUIREMENTS = open(op.join(CURDIR, 'requirements.txt')).readlines()

if sys.version_info < (2, 7):
    REQUIREMENTS.append('importlib')


setup(
    name=NAME,
    version=MODULE.__version__,
    license=MODULE.__license__,
    author=MODULE.__author__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    platforms=('Any'),
    keywords="mercurial git static revision django flask".split(),

    author_email='horneds@gmail.com',
    url=' http://github.com/klen/dealer',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Environment :: Console',
    ],

    packages=['dealer', 'dealer.contrib', 'dealer.contrib.django'],
    install_requires=REQUIREMENTS,
)

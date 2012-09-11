# -*- coding: utf-8 -*-
"""
    Dealer
    ======

    Dealer tools for watching SCM.

"""

__version__ = '0.1.0'
__project__ = __name__
__author__ = "Kirill Klenov <horneds@gmail.com>"
__license__ = "BSD"


DEFAULT_SCM = 'git'


class Dealer:

    def __init__(self, scm=None):
        self.scm = scm or DEFAULT_SCM

    def init_app(self):
        pass

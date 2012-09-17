# -*- coding: utf-8 -*-
"""
    Dealer
    ======

    Dealer tools for watching SCM.

"""

__version__ = '0.1.8'
__project__ = __name__
__author__ = "Kirill Klenov <horneds@gmail.com>"
__license__ = "BSD"


def get_backend(name, **kwargs):
    " Create backend by name. "

    from importlib import import_module

    mod = import_module(__name__ + '.' + name)
    return mod.Backend(**kwargs)

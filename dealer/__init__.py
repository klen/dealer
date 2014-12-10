# -*- coding: utf-8 -*-

""" description.

Dealer
======

The module for watching SCM (git, hg, svn).
Use it for control a static's versions.

"""

__version__ = '2.0.4'
__project__ = __name__
__author__ = "Kirill Klenov <horneds@gmail.com>"
__license__ = "BSD"


def get_backend(name, **kwargs):
    """ Create backend by name.

    :return Backend:

    """
    from importlib import import_module

    mod = import_module(__name__ + '.' + name)
    return mod.Backend(**kwargs)

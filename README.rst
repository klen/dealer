Dealer
######

Dealer — SCM_ revision helper in your projects. Just add SCM_ revision to
your static paths and get automatic control at client browser caches:

Somewhere in templates: ::
    
    <script src='/main.js?{{ request.revision }}'

On clientside: ::

    <script src='/main.js?34jhfd45hd8'

Supported Git_, Mercurial_ and simple revision parse by file.

.. note:: For Mercurial support install mercurial

.. image:: https://secure.travis-ci.org/klen/dealer.png?branch=develop
    :target: http://travis-ci.org/klen/dealer
    :alt: Build Status

.. contents::

Requirements
=============

- python >= 2.6

Installation
=============

**Dealer** should be installed using pip: ::

    pip install dealer

Usage
=====

Basic usage
-----------
::

    from dealer.git import git

    print git.revision

::

    # Auto parse repository type
    from dealer.auto import auto
    print auto.revision


Manualy create backend
----------------------

**path** — path to SCM_ repository (current dir by default)
::
    from dealer.mercurial import Backend

    hg = Backend('/path/to/hg/repo')


Django support
--------------

Settings
^^^^^^^^

*DEALER_TYPE* — Type of SCM_ repository ('auto', 'git', 'mercurial', 'simple'). By default 'auto'
*DEALER_PATH* — Path to SCM_. By default current dir


Context-processor
^^^^^^^^^^^^^^^^^

Append to your settings: ::

    TEMPLATE_CONTEXT_PROCESSORS += 'dealer.contrib.django.staff.context_processor',

And use *REVISION* variable in your templates: ::

    <link href="/test.css?{{ REVISION }}" rel="stylesheet" type="text/css" media="screen" />
    <script src="/test.js?{{ REVISION }}"></script>

Middleware
^^^^^^^^^^
    
Append to your settings: ::

    MIDDLEWARE_CLASSES += 'dealer.contrib.django.staff.middleware',

And use in your views: ::

    def view(request):
        return request.revision

Or in your templates by `request.revision` var.


Flask support
-------------

Settings
^^^^^^^^

*DEALER_TYPE* — Type of SCM_ repository ('auto', 'git', 'mercurial', 'simple'). By default 'auto'
*DEALER_PARAMS* — Params for backend

Usage
^^^^^

In views::

        from flask import Flask, g
        from dealer.contrib.flask import Dealer

        app = Flask('test')
        Dealer(app)
        assert app.revision

        @app.route('/')
        def usage_in_view():
            return g.revision


In templates: ::

    <link href="/test.css?{{ REVISION }}" rel="stylesheet" type="text/css" media="screen" />


Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/Dealer/issues


Contributing
============

Development of dealer happens at github: https://github.com/klen/Flask-Mixer


Contributors
=============

* klen_ (Kirill Klenov)


License
=======

Licensed under a `BSD license`_.


.. _BSD license: http://www.linfo.org/bsdlicense.html
.. _klen: http://klen.github.com/
.. _SCM: http://en.wikipedia.org/wiki/Source_Control_Management
.. _Git: http://en.wikipedia.org/wiki/Git_(oftware)
.. _Mercurial: http://en.wikipedia.org/wiki/Mercurial

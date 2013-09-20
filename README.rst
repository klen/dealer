|logo| Dealer
#############

.. _description:

Dealer — SCM_ revision helper in your projects. Just add SCM_ revision to
your static paths and get automatic control at client browser caches:

Somewhere in templates: ::
    
    <script src='/main.js?{{ request.revision }}'

On clientside: ::

    <script src='/main.js?34jhfd45hd8'

Supported Git_, Mercurial_ and simple revision parse by file.

.. note:: You should install Mercurial_ for hg support.


.. _badges:

.. image:: https://secure.travis-ci.org/klen/dealer.png?branch=develop
    :target: http://travis-ci.org/klen/dealer
    :alt: Build Status

.. image:: https://coveralls.io/repos/klen/dealer/badge.png?branch=develop
    :target: https://coveralls.io/r/klen/dealer
    :alt: Coverals

.. image:: https://pypip.in/v/dealer/badge.png
    :target: https://crate.io/packages/dealer
    :alt: Version

.. image:: https://pypip.in/d/dealer/badge.png
    :target: https://crate.io/packages/dealer
    :alt: Downloads

.. image:: https://dl.dropboxusercontent.com/u/487440/reformal/donate.png
    :target: https://www.gittip.com/klen/
    :alt: Donate


.. _contents:

.. contents::


.. _requirements:

Requirements
=============

- python (2.6, 2.7, 3.3)


.. _installation:

Installation
=============

**Dealer** should be installed using pip: ::

    pip install dealer


.. _usage:

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

**DEALER_TYPE** — Type of SCM_ repository ('auto', 'git', 'mercurial', 'simple', 'null'). By default 'auto';

**DEALER_PATH** — Path to SCM_. By default current dir;

**DEALER_SILENT** — Disable log warnings;

**DEALER_BACKENDS** — Backends for auto search by default ('git', 'mercurial', 'simple', 'null');


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

    MIDDLEWARE_CLASSES += 'dealer.contrib.django.staff.Middleware',

And use in your views: ::

    def view(request):
        return request.revision

Or in your templates by `request.revision` var.


Flask support
-------------

Settings
^^^^^^^^

*DEALER_TYPE* — Type of SCM_ repository ('auto', 'git', 'mercurial', 'simple', 'silent'). By default 'auto'
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


.. _bagtracker:

Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/Dealer/issues


.. _contributing:

Contributing
============

Development of dealer happens at github: https://github.com/klen/dealer


.. _contributors:

Contributors
=============

* klen_ (Kirill Klenov)


.. _license:

License
=======

Licensed under a `BSD license`_.


.. _links:

.. _BSD license: http://www.linfo.org/bsdlicense.html
.. _klen: http://klen.github.com/
.. _SCM: http://en.wikipedia.org/wiki/Source_Control_Management
.. _Git: http://en.wikipedia.org/wiki/Git_(oftware)
.. _Mercurial: http://en.wikipedia.org/wiki/Mercurial
.. |logo| image:: https://raw.github.com/klen/dealer/develop/docs/_static/logo.png
                  :width: 100

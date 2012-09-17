from __future__ import absolute_import

from flask import g

from .. import get_backend


class Dealer():
    """This class is used for integration to one or more Flask
    applications.

    :param app: Flask application

    ::

        app = Flask(__name__)
        dealer = Dealer(app)

    The second possibility is to create the object once and configure the
    application later to support it::

        dealer = Dealer()
        ...
        dealer.init_app(app)

    """

    def __init__(self, app=None):
        self.type = 'auto'
        self.params = dict()
        self.backend = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        """This callback can be used to initialize an application for the
        use with this dealer setup.

        See :ref:`configuration`.

        :param app: Flask application
        """
        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        app.extensions['dealer'] = self
        self.type = app.config.get('DEALER_TYPE', 'auto')
        self.params = app.config.get('DEALER_PARAMS', dict())
        self.backend = backend = get_backend(self.type, **self.params)

        app.context_processor(lambda: dict(REVISION=backend.revision))
        app.revision = backend.revision

        def path_g():
            g.revision = backend.revision

        app.before_first_request(path_g)

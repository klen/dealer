""" Django support. """

from .settings import BACKEND


def context_processor(request):
    """ Append current SCM revision to template context.

    :return dict: A context with revision and tag.

    """
    return dict(REVISION=BACKEND.revision, TAG=BACKEND.tag)


class Middleware:

    """ Append current SCM revision to request object. """

    __slots__ = 'get_response',

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """ Add revision and tag to request. """
        request.revision = BACKEND.revision
        request.tag = BACKEND.tag
        return self.get_response(request)

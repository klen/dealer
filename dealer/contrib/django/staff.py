""" Django support. """

from .settings import BACKEND


def context_processor(request):
    """ Append current SCM revision to template context.

    :return dict: A context with revision and tag.

    """
    return dict(REVISION=BACKEND.revision, TAG=BACKEND.tag)


class Middleware(object):

    """ Append current SCM revision to request object. """

    @staticmethod
    def process_request(request):
        """ Add revision and tag to request. """
        request.revision = BACKEND.revision
        request.tag = BACKEND.revision

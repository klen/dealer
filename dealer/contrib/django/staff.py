from .settings import BACKEND


def context_processor(request):
    " Append current SCM revision to template context. "

    return dict(REVISION=BACKEND.revision, TAG=BACKEND.tag)


class Middleware:
    " Append current SCM revision to request object. "

    @staticmethod
    def process_request(request):
        request.revision = BACKEND.revision
        request.tag = BACKEND.revision

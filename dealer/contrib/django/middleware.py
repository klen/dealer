from .settings import BACKEND


class Dealer:
    " Append current SCM revision to request object. "

    @staticmethod
    def process_request(request):
        request.revision = BACKEND.revision

from .settings import BACKEND


def scm_revision(request):
    " Append current SCM revision to template context. "

    return dict(REVISION=BACKEND.revision)

import abc
import logging


logger = logging.getLogger('DEALER')


class SCMBackend(object):
    " Abstract SCM Backend. "

    __meta__ = abc.ABCMeta

    def __init__(self, path=None, **options):
        self.path = path
        self.options = options

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path
        self._repo = None
        self._revision = None

    @property
    def repo(self):
        return self._repo or self.init_repo()

    @property
    def revision(self):
        return self.repo and self._revision

    @abc.abstractmethod
    def init_repo(self):
        pass


# pymode:lint_ignore=W0201

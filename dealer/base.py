"""Abstract backend support."""

import abc
import logging


logger = logging.getLogger('DEALER')


class SCMBackend(object):

    """Abstract SCM Backend."""

    __meta__ = abc.ABCMeta

    def __init__(self, path=None, **options):
        """Init backend."""
        self.path = path
        self.options = options

    @property
    def path(self):
        """Get path to SCM.

        :return str:

        """
        return self._path

    @path.setter
    def path(self, path):
        """Set path and clean current state."""
        self._path = path
        self._repo = None
        self._revision = None
        self._tag = None
        self._branch = None

    @property
    def repo(self):
        """Cache repository.

        :return object: A repo
        """
        return self._repo or self.init_repo()

    @property
    def revision(self):
        """Get current revision.

        :return str:
        """
        return self.repo and _to_str(self._revision)

    @property
    def tag(self):
        """Get current tag.

        :return str:
        """
        return self.repo and _to_str(self._tag)

    @property
    def branch(self):
        """Get current branch.

        :return str:
        """
        return self.repo and _to_str(self._branch)

    @abc.abstractmethod
    def init_repo(self):
        """Initialize repository."""
        raise NotImplementedError


def _to_str(obj):
    if not isinstance(obj, str) and obj is not None:
        return obj.decode()
    return obj

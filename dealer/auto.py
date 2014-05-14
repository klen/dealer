""" Select backend automaticaly. """

from .base import SCMBackend


class Backend(SCMBackend):

    """ Check path and select backend automaticaly. """

    default_backends = 'git', 'mercurial', 'simple', 'env', 'null'

    def __init__(self, **kwargs):
        """ Init backend. """
        super(Backend, self).__init__(**kwargs)
        self._backend = None

    def init_repo(self):
        """ Check path.

        :return object: A repo
        :raise TypeError: Supported backend not found.

        """
        from importlib import import_module

        backends = self.options.get('backends') or self.default_backends
        for mod_name in backends:
            mod = import_module('dealer.' + mod_name)
            try:
                self._backend = mod.Backend(self.path, **self.options)
                assert self._backend.repo
                break

            except (TypeError, ImportError, AssertionError):
                continue

        if self._backend:
            self._repo = self._backend.repo
            self._revision = self._backend.revision
            self._tag = self._backend.tag
            return self._repo

        raise TypeError('Invalid project: {0}'.format(self.path))


auto = Backend()

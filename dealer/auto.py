from .base import SCMBackend


class Backend(SCMBackend):

    default_backends = 'git', 'mercurial', 'simple'

    def __init__(self, **kwargs):
        super(Backend, self).__init__(**kwargs)
        self._backend = None

    def init_repo(self):
        from importlib import import_module

        backends = self.options.get('backends') or self.default_backends
        for mod_name in backends:
            mod = import_module('dealer.' + mod_name)
            try:
                self._backend = mod.Backend(self.path, **self.options)
                break

            except (TypeError, ImportError):
                continue

        if not self._backend:
            raise TypeError('Invalid repository.')

        self._repo = self._backend.repo
        self._revision = self._backend.revision

        return self._repo


auto = Backend()


# pymode:lint_ignore=W0201

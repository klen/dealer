from .base import SCMBackend


class Backend(SCMBackend):

    def __init__(self, **kwargs):
        super(Backend, self).__init__(**kwargs)
        self._backend = None

    def init_repo(self):
        from . import git, mercurial, simple

        for mod in (git, mercurial, simple):
            try:
                self._backend = mod.Backend(self.path, **self.options)
                break

            except TypeError:
                continue

        if not self._backend:
            raise TypeError('Invalid repository.')

        self._repo = self._backend.repo
        self._revision = self._backend.revision

        return self._repo


auto = Backend()


# pymode:lint_ignore=W0201

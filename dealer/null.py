from .base import SCMBackend


class Backend(SCMBackend):

    def init_repo(self):
        self._repo = self
        self._revision = 'null'
        return self


null = Backend()


# pymode:lint_ignore=W0201

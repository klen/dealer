from __future__ import absolute_import

from .base import SCMBackend

try:
    from mercurial import ui, hg as HG, error

    class Backend(SCMBackend):
        " Mercurial backend. "

        def init_repo(self):
            try:
                self._repo = HG.repository(ui.ui(), path=self.path or '.')
                self._revision = self._repo[len(self._repo) - 1].hex()
            except error.RepoError:
                raise TypeError('Mercurial repository not found.')

            return self._repo

except ImportError:

    class Backend(SCMBackend):

        @staticmethod
        def init_repo():
            raise TypeError('Mercurial not installed.')


hg = Backend()


# pymode:lint_ignore=W0201

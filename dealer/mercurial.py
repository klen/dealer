from __future__ import absolute_import

from mercurial import ui, hg as HG, error

from .base import SCMBackend


class Backend(SCMBackend):
    " Mercurial backend. "

    def init_repo(self):
        try:
            self._repo = HG.repository(ui.ui(), path=self.path or '.')
            self._revision = self._repo[len(self._repo) - 1].hex()
        except error.RepoError:
            raise TypeError('Mercurial repository not found.')

        return self._repo


hg = Backend()


# pymode:lint_ignore=W0201

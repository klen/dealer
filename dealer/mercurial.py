from __future__ import absolute_import

from .base import SCMBackend, logger

try:
    from mercurial import ui, hg as HG, error  # nolint

    class Backend(SCMBackend):
        " Mercurial backend. "

        def init_repo(self):
            try:
                self._repo = HG.repository(ui.ui(), path=self.path or '.')
                self._revision = self._repo[len(self._repo) - 1].hex()
            except error.RepoError:
                message = 'Mercurial repository not found: {0}'.format(
                    self.path)
                if not self.options.get('silent'):
                    logger.error(message)

                raise TypeError(message)

            return self._repo

except ImportError:

    class Backend(SCMBackend):

        def init_repo(self):
            message = 'Mercurial is not installed.'
            if not self.options.get('silent'):
                logger.error(message)

            raise TypeError(message)


hg = Backend()


# pymode:lint_ignore=W0201

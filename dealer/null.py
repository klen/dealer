from .base import SCMBackend, logger


class Backend(SCMBackend):

    def init_repo(self):
        self._repo = self
        self._revision = 'null'
        logger.warning('Dealer uses "null" revision.')
        return self


null = Backend()


# pymode:lint_ignore=W0201

from __future__ import absolute_import

from git import Repo, InvalidGitRepositoryError, NoSuchPathError # nolint

from .base import SCMBackend, logger


class Backend(SCMBackend):
    " Git backend. "

    def init_repo(self):
        try:
            self._repo = Repo(self.path)
            self._revision = self.repo.head.commit.hexsha
            return self._repo

        except (InvalidGitRepositoryError, NoSuchPathError):
            message = 'Git repository not found: {0}'.format(self.path)
            if not self.options.get('silent'):
                logger.error(message)

            raise TypeError(message)


git = Backend()


# pymode:lint_ignore=W0201

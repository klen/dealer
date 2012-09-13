from __future__ import absolute_import

from git import Repo, InvalidGitRepositoryError, NoSuchPathError

from .base import SCMBackend


class Backend(SCMBackend):
    " Git backend. "

    def init_repo(self):
        try:
            self._repo = Repo(self.path)
            self._revision = self.repo.head.commit.hexsha
            return self._repo

        except (InvalidGitRepositoryError, NoSuchPathError):
            raise TypeError('Git repository not found.')


git = Backend()


# pymode:lint_ignore=W0201

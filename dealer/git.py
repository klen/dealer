""" Git support. """

from __future__ import absolute_import

from os import path as op, name, getcwd

from subprocess import Popen, PIPE

from .base import SCMBackend, logger


class GitException(Exception):

    """ Exception for git related errors. """

    pass


class GitRepo(object):

    """ Initialize Git repository. """

    git_cmd = 'git'

    def __init__(self, path):
        """ Init backend. """
        self.path = path or getcwd()

        if not op.isdir(self.path):
            self.path = op.dirname(self.path)

        if not op.exists(self.path):
            raise GitException('Path doesnt exists: %s' % self.path)

    def git(self, cmd, stderr=PIPE, stdout=PIPE, **kwargs):
        """ Run git command.

        :return str: The command output.

        """
        cmd = ' '.join((self.git_cmd, cmd))

        try:
            proc = Popen(
                cmd.split(), stderr=stderr, stdout=stdout,
                close_fds=(name == 'posix'), cwd=self.path, **kwargs)

        except OSError:
            raise GitException('Git not found.')

        stdout, stderr = [s.strip() for s in proc.communicate()]  # noqa
        status = proc.returncode
        if status:
            raise GitException(stderr)

        return stdout


class Backend(SCMBackend):

    """ Git backend. """

    def init_repo(self):
        """ Initialize self repo.

        :return GitRepo:

        """
        try:
            self._repo = GitRepo(self.path)
            self._revision = self.repo.git('log -1 --format=%h')
            self._tag = self.repo.git('describe --always --tags')
            return self._repo

        except GitException as e:
            if not self.options.get('silent'):
                logger.error(e)

            raise TypeError(e)


git = Backend()

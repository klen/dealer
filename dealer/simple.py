""" Get revision from file. """

from .base import SCMBackend, logger


class Backend(SCMBackend):

    """ Get revision from file. """

    default_filename = '.revision'

    def init_repo(self):
        """ Read revision from file.

        :return Backend:

        """
        from os import path as op

        try:
            assert op.exists(self.path or '')

            self._repo = self
            filename = self.options.get('filename') or self.default_filename
            rev_file = self.path if op.isfile(
                self.path) else op.join(self.path, filename)
            with open(rev_file) as f:
                self._tag = self._revision = f.read().strip()
        except (AssertionError, IOError):
            message = 'Invalid path: {0}'.format(self.path)
            if not self.options.get('silent'):
                logger.error(message)

            raise TypeError(message)

        return self._repo


simple = Backend()

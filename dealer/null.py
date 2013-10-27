""" Dummy backend. """

from .base import SCMBackend, logger


class Backend(SCMBackend):

    """ Always return null. """

    def init_repo(self):
        """ Set null.

        :return Backend:

        """
        self._repo = self
        self._revision = 'null'
        self._tag = 'null'
        logger.warning('Dealer uses "null" revision.')
        return self


null = Backend()

""" Get revision from local environment. """

from .base import SCMBackend, logger


class Backend(SCMBackend):

    """ Get revision from local environment variable. """

    default_revision_env_keyname = 'DEALER_REVISION'
    default_tag_env_keyname = 'DEALER_TAG'

    def init_repo(self):
        """ Read revision from local environment variable.

        :return Backend:

        """
        from os import environ
        self._repo = self

        try:
            revision_env_keyname = self.options.get(
                'revision_env_keyname') or self.default_revision_env_keyname
            assert (revision_env_keyname in environ and environ[revision_env_keyname] != '') # noqa
            self._revision = environ[revision_env_keyname]
        except AssertionError:
            message = 'Environment variable {0} not found'.format(
                revision_env_keyname)
            if not self.options.get('silent'):
                logger.error(message)

            raise TypeError(message)

        try:
            tag_env_keyname = self.options.get(
                'tag_env_keyname') or self.default_tag_env_keyname
            assert (
                tag_env_keyname in environ and environ[tag_env_keyname] != '')
            self._tag = environ[tag_env_keyname]
        except AssertionError:
            message = 'Environment variable {0} not found'.format(
                tag_env_keyname)
            if not self.options.get('silent'):
                logger.error(message)

            raise TypeError(message)

        return self._repo


env = Backend()


# pymode:lint_ignore=W0201

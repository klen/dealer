from django.conf import settings
from dealer import get_backend


TYPE = getattr(settings, 'DEALER_TYPE', 'auto')
PATH = getattr(settings, 'DEALER_PATH', None)
FILENAME = getattr(settings, 'DEALER_FILENAME', None)
BACKENDS = getattr(settings, 'DEALER_BACKENDS', None)


BACKEND = get_backend(TYPE, path=PATH, filename=FILENAME, backends=BACKENDS)

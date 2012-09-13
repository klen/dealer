from django.conf import settings
from dealer import get_backend


TYPE = getattr(settings, 'DEALER_TYPE', 'auto')
PATH = getattr(settings, 'DEALER_PATH', None)


BACKEND = get_backend(TYPE, path=PATH)

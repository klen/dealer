""" Integrate dealer to pyramid. """
from __future__ import absolute_import

from dealer import get_backend


DEFAULTS = {
    'backends': None,
    'filename': None,
    'path': None,
    'silent': True,
    'type': 'auto',
}


def dealer_context(event):
    """ Update template context. """
    from pyramid.threadlocal import get_current_registry
    registry = get_current_registry()
    dealer = registry.dealer
    event.rendering_val['DEALER_REVISION'] = str(dealer.revision)
    event.rendering_val['DEALER_TAG'] = str(dealer.tag)


def includeme(config):
    """ Setup the dealer. """
    settings = dict(DEFAULTS)
    settings.update(dict(
        (key.split('.', 1)[1], value)
        for key, value in config.registry.settings.items()
        if key.startswith('dealer.')
    ))
    config.registry.settings['dealer'] = settings
    config.registry.dealer = get_backend(
        settings['type'], path=settings['path'], filename=settings['filename'],
        backends=settings['backends'], silent=settings['silent'],
    )

    config.add_subscriber(dealer_context, 'pyramid.events.BeforeRender')

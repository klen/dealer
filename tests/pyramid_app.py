from pyramid.config import Configurator
from pyramid.renderers import render_to_response
import os.path as op


def revision(request):
    return render_to_response(
        op.dirname(op.abspath(__file__)) + '/test.jinja2', {}, request=request)

config = Configurator()
config.registry.settings['dealer.context'] = True
config.include('dealer.contrib.pyramid')
config.include('pyramid_jinja2')
config.add_route('revision', '/revision')
config.add_view(revision, route_name='revision')

app = config.make_wsgi_app()

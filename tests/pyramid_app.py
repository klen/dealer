from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.renderers import render_to_response


def revision(request):
    return render_to_response('test.jinja2', {}, request=request)

config = Configurator()
config.include('dealer.contrib.pyramid')
config.include('pyramid_jinja2')
config.add_route('revision', '/revision')
config.add_view(revision, route_name='revision')

app = config.make_wsgi_app()

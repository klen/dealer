from django.conf.urls import patterns
from django.http import HttpResponse


urlpatterns = patterns(
    '',
    ('^revision/', lambda r: HttpResponse(r.revision)),
    ('^tag/', lambda r: HttpResponse(r.tag))
)

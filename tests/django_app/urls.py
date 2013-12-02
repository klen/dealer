from django.http import HttpResponse
from django.conf.urls import patterns


urlpatterns = patterns(
    '',
    ('^revision/', lambda r: HttpResponse(r.revision)),
    ('^tag/', lambda r: HttpResponse(r.tag))
)

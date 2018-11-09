from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns = [
    path('revision/', lambda r: HttpResponse(r.revision)),
    path('tag/', lambda r: HttpResponse(r.tag)),
    path('template/', lambda r: render(r, 'template')),
]

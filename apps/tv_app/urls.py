from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.newshows),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<num>\d+)/delete$', views.delete),
    url(r'^shows/(?P<num>\d+)/edit$', views.edit),
    url(r'^shows/(?P<num>\d+)$', views.showtab),
]

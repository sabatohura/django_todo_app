from django.conf.urls import url
from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    url(r'^$',views.index, name= 'index'),
    url(r'^details/(?P<id>w{0,50})/$', views.details, name='details')
]   

from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^foo', views.foo, name='foo'),
    url(r'^mygetview', views.mygetview, name='mygetview'),
    url(r'^mypostview', views.mypostview, name='mypostview'),
    url(r'^myajaxview', views.myajaxview, name='myajaxview'),
    url(r'^myajaxformview', views.myajaxformview, name='myajaxformview'),
    #url(r'^formview1', views.formview1, name='formview1'),
    #url(r'^register', views.register, name='register'),
    #url(r'^login', views.user_login, name='login'),
    #url(r'^$', ThingList.as_view(), name='thing_list'),
    #url(r'^new/$', ThingCreate.as_view(), name='thing_create'),
    #url(r'^(?P<pk>\d+)/$', ThingDetail.as_view(), name='thing_detail'),
    #url(r'^(?P<pk>\d+)/update/$', ThingUpdate.as_view(), name='thing_update'),
    #url(r'^(?P<pk>\d+)/delete/$', ThingDelete.as_view(), name='thing_delete'),
]

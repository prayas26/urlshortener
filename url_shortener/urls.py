from django.conf.urls import patterns, include, url
from django.contrib import admin
from shorturls.views import *

urlpatterns = patterns('',
	url(r'^$', LinkCreate.as_view(), name='home'),
	url(r'^(?P<short_url>\w+)$', RedirectToLongURL.as_view(), name='redirect_short_url'),
	url(r'^link/(?P<pk>\w+)$', LinkShow.as_view(), name='link_show'),
    url(r'^login/', include(admin.site.urls)),
    url(r'^mygift2/', mygift2),
)
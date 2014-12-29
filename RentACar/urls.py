from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

   # url(r'^RentACar/', include('RentACar.urls')),
    url(r'^$', 'RentACar.views.home1', name='home1'),
    url(r'^about$', 'RentACar.views.about', name='about'),
    url(r'^register$', 'RentACar.views.register'),
    url(r'^navbar$', 'RentACar.views.navbar'),
    url(r'^result', 'RentACar.views.result'),
    url(r'^rent', 'RentACar.views.rent'),




    url(r'^admin/', include(admin.site.urls)),




)




"""
Definition of urls for Fizzyb.
"""

from django.conf.urls import include, url
import Counter.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', Counter.views.index, name='index'),
    url(r'^home$', Counter.views.index, name='home'),
    ]
    # Examples:
    # url(r'^$', Fizzyb.views.home, name='home'),
    # url(r'^Fizzyb/', include('Fizzyb.Fizzyb.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),


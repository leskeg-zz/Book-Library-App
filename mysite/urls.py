from django.conf.urls import patterns, include, url
from myapp.myapi import *
from django.conf import settings
from django.conf.urls.static import static


book_resource = BookResource()
publisher_resource = PublisherResource()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'myapp.views.index'),
    url(r'^books/', include(book_resource.urls)),
    url(r'^publishers/', include(publisher_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^base/', include('firstapp.urls')),

)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

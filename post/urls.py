from django.conf.urls import url
from post.views import EntryUpdateView,custom_login,custom_logout,EntryDetailView,EntryDeleteView,EntryUpdateView,EntryFormView,EntryView,EntryArchieveAprilView,EntryArchieveMarchView
from .models import Entry
from . import views


urlpatterns = [
    url(r'^$',EntryView.as_view(), name="base"),
    url(r'^index/', EntryFormView.as_view(), name="index"),
    url(r'^archieve/april2015/', EntryArchieveAprilView.as_view() ,name="archiveapril"),
    url(r'^archieve/march2015/', EntryArchieveMarchView.as_view() ,name="archivemarch"),
    url(r'login/$', views.custom_login , name = 'login'),
    url(r'logout/$','django.contrib.auth.views.logout',{'next_page' : '/out'}, name="realout"),
    url(r'out/$', views.custom_logout, name="out"),
    url(r'loggedin/$', views.loggedin, name="successfullog"),
    url(r'auth/$', views.auth_view ,name="auth"),
    url(r'^(?P<pk>\d+)/update/$', EntryUpdateView.as_view(),
        name='entry_update'),
    url(r'^(?P<pk>\d+)/$', EntryDetailView.as_view(),name='entry_detail'),
     url(r'^(?P<pk>\d+)/delete/$', EntryDeleteView.as_view(), name='entry_delete'),
]

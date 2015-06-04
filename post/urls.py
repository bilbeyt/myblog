from django.conf.urls import url
from post.views import EntryUpdateView,custom_login,custom_logout,\
EntryDetailView,EntryDeleteView,EntryCreateView,EntryListView
from .models import Entry
from . import views


urlpatterns = [
    url(r'^$', EntryListView.as_view(), name="base"),
    url(r'^create/',
        EntryCreateView.as_view(),
        name="create"),
    url(r'login/$',
        views.custom_login ,
        {'next_page':'base'},
        name = 'login'),
    url(r'logout/$',
        views.custom_logout,
        name="realout"),
    url(r'auth/$',
        views.auth_view,
        name="auth"),
    url(r'^(?P<slug>[\w-]+)/update/$',
        EntryUpdateView.as_view(),
        name='entry_update'),
    url(r'^(?P<slug>[\w-]+)/$',
        EntryDetailView.as_view(),
        name='entry_detail'),
    url(r'^(?P<slug>[\w-]+)/delete/$',
        EntryDeleteView.as_view(),
        name='entry_delete'),
]

from django.conf.urls import url
from post.views import custom_login,custom_logout,EntryFormView,EntryView,EntryArchieveAprilView,EntryArchieveMarchView
from .models import Entry
from . import views


urlpatterns = [
    url(r'^$',EntryView.as_view(), name="base"),
    url(r'^index/', EntryFormView.as_view()),
    url(r'^archieve/april2015/', EntryArchieveAprilView.as_view()),
    url(r'^archieve/march2015/', EntryArchieveMarchView.as_view()),
    url(r'login/$', views.custom_login , name = 'login'),
    url(r'logout/$','django.contrib.auth.views.logout',{'next_page' : '/out'}),
    url(r'out/$', views.custom_logout),
    url(r'loggedin/$', views.loggedin),
    url(r'auth/$', views.auth_view ,name="auth")

]

from django.conf.urls import url
from post.views import EntryFormView,EntryView,EntryArchieveAprilView,EntryArchieveMarchView
from .models import Entry
from . import views

urlpatterns = [
    url(r'^$',EntryView.as_view()),
    url(r'^index/', EntryFormView.as_view()),
    url(r'^archieve/april2015/', EntryArchieveAprilView.as_view()),
    url(r'^archieve/march2015/', EntryArchieveMarchView.as_view()),
]

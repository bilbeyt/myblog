from django.conf.urls import url
from firstapp.views import CommentsFormView,CommentsView,CommentsArchieveAprilView,CommentsArchieveMarchView
from .models import Comments
from . import views

urlpatterns = [

    url(r'index/', CommentsFormView.as_view(template_name="index.html")),
    url(r'result/',CommentsView.as_view()),
    url(r'archieve/april2015', CommentsArchieveAprilView.as_view()),
    url(r'archieve/march2015', CommentsArchieveMarchView.as_view()),
]

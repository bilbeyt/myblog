from django import forms
from .models import Comments
import datetime

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','title','content')

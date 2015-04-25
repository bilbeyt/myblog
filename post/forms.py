from django import forms
from .models import Entry
import datetime

class EntryCreateForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('name','title','content')

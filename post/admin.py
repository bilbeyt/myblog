from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    fields = ['author','title','content']
    list_display = ('author','title','pub_date')
    list_filter = ['pub_date','author']
    search_fields = ['author','title']


admin.site.register(Entry,EntryAdmin)

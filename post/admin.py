from django.contrib import admin
from .models import Entry



class EntryAdmin(admin.ModelAdmin):
    fields = ['name','title','content','pub_date']
    list_display = ('name','title','pub_date','was_published_recently')
    list_filter = ['pub_date','name']
    search_fields = ['name','title']



admin.site.register(Entry,EntryAdmin)
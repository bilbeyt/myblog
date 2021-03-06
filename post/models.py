from django.db import models
from django.utils import timezone
import datetime
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


class Entry(models.Model):
    title= models.CharField(_("title"),max_length=100)
    content = RichTextField(_("content"))
    pub_date = models.DateTimeField(_("publish time"),auto_now_add=True)
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=100)
    file = models.FileField(_("file"), upload_to="files/",blank="True")

    def __unicode__(self):
        return self.content


@receiver(pre_save,sender=Entry)
def entry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)




 

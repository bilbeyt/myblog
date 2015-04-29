from django.db import models
from django.utils import timezone
import datetime
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User





class Entry(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


    def __unicode__(self):
        return self.content


@receiver(pre_save,sender=Entry)
def entry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)



 

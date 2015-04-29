from django.db import models
from django.utils import timezone
import datetime
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver





class Entry(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField('Publish time', default = datetime.datetime.now())
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


    def __unicode__(self):
        return self.content

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

@receiver(pre_save,sender=Entry)
def entry_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.title)

'''
    def save(self, *args, **kwargs):
        if not self.id:

            self.slug = slugify(self.title)

        super(Entry, self).save(*args, **kwargs)
'''


 

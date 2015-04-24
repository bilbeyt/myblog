from django.db import models
from django.utils import timezone
import datetime


class Comments(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField('Publish time', default = datetime.datetime.now())
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.content

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
 

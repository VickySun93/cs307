from django.db import models
from time import time

# Create your models here.
class Article(models.Model):
        title = models.CharField(max_length=200)
        body = models.TextField()
        pub_date = modelsDateTimeField('date published')
        likes = models.IntegerField(default=0)
        thumbnail = models.FileField(upload_to=get_upload_file_name)

        def __unicode__(self):
                return self.title

class Comment(models.Model):
                name = models.CharField(max_length=200)
                body = models.TextField()
                pub_date = models.DateTimeField('date published')
                article = models.ForeignKey(Article)

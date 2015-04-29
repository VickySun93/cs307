from django.db import models
from django.contrib.auth.models import User  

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sendedMessages', verbose_name='from')
    recipient = models.ForeignKey(User, related_name='inboxMessages', verbose_name='to')
    content = models.CharField(max_length=100, verbose_name='message')
    isDeleted = models.BooleanField(default=False, verbose_name='deleted')

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

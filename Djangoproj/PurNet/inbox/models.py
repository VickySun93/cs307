from django.db import models
import datetime
from django.utils import timezone
from create_acct.models import Site_User
from course_mang.models import Course

class Inbox_Message(models.Model):
	msg_owner=models.ForeignKey(Site_User)
	msg_members=models.ManyToManyField(Site_User)
	msg_text=models.CharField(max_length=1000)
	msg_orig_date=models.DateTimeField('date sent')
	msg_subject=models.CharField(max_length=100)
	def __str__(self):
		return str(self.id)

class Inbox_Response(models.Model):
	msg_parent=models.ForeignKey(Inbox_Message)
	resp_text=models.CharField(max_length=1000)
	resp_date=models.DateTimeField('date replied')
	resp_owner=models.ForeignKey(Site_User)
from django.db import models
import datetime
from django.utils import timezone
from authy.models import Site_User
from course_mang.models import Course
from group_mang.models import Site_Group

class Forum_Question(models.Model):
	thread_owner=models.ForeignKey(Site_User)
	thread_course=models.ForeignKey(Course)
	thread_group=models.ForeignKey(Site_Group)
	thread_title = models.CharField(max_length=100)
	question_text = models.CharField(max_length=1000)
	ques_date = models.DateTimeField('date published')
	def __str__(self):
		return str(self.id)

class Forum_Response(models.Model):
	response_owner=models.ForeignKey(Site_User)
	forum_question=models.ForeignKey(Forum_Question)
	response_text=models.CharField(max_length=2000)
	resp_date=models.DateTimeField('date published')
	def __str__(self):
		return str(self.id)

# Create your models here.

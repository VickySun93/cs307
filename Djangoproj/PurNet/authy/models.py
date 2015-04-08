from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from course_mang.models import Course
#from django.conf import settings as django_settings
import os.path

class Site_User(models.Model):
	user = models.OneToOneField(User)
	courses=models.ManyToManyField(Course)
	def __str__(self):
		return str(self.id)

from django.db import models
import datetime
from django.utils import timezone
from course_mang.models import Course
from django.contrib.auth.models import User



class Site_User(models.Model):
	user = models.OneToOneField(User)
# 	name = models.CharField(max_length=50)
# 	username = models.CharField(max_length=16, unique=True)
# 	email = models.CharField(max_length=30)
# 	password = models.CharField(max_length=40)
	courses=models.ManyToManyField(Course)
	def __str__(self):
		return str(self.id)
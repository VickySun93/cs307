from django.db import models
import datetime
from django.utils import timezone
from course_mang.models import Course



class User(models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=16, unique=True)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=40)
	courses=models.ManyToManyField(Course)
	def __str__(self):
		return self.id
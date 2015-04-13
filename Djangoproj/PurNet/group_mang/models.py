from django.db import models
from authy.models import Site_User

# Create your models here.
class Group_Admin(models.Model):
	admin_members= models.ManyToManyField(Site_User)

class Site_Group(models.Model):
	group_title = models.CharField(max_length=50)
	group_desc = models.CharField(max_length= 1000)
	group_admins = models.OneToOneField(Group_Admin)
	group_members = models.ManyToManyField(Site_User)
	def __str__(self):
		return self.group_title
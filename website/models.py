from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	is_individual = models.BooleanField(default=False)
	is_company = models.BooleanField(default=False)
	is_verified = models.BooleanField(default=False)
	def __str__(self):
		return self.email

class individual(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	state = models.TextField(max_length=500, blank=True)
	def __str__(self):
		return self.state

class company(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	state = models.CharField(max_length=500, blank=True)
	city = models.CharField(max_length=500, blank=True)

	def __str__(self):
		return self.state


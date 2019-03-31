from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
	is_individual = models.BooleanField(default=False)
	is_company = models.BooleanField(default=False)
	is_verified = models.BooleanField(default=False)
	individual = models.ForeignKey('individual',null=True, on_delete=models.CASCADE)
	company = models.ForeignKey('company',null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.email

class individual(models.Model):
	working_industry = models.TextField(max_length=500, blank=True)
	if_other = models.TextField(max_length=500, blank=True)
	phone_number = PhoneNumberField()

	def __str__(self):
		return str(self.phone_number)

class company(models.Model):
	state = models.CharField(max_length=500, blank=True)
	city = models.CharField(max_length=500, blank=True)

	def __str__(self):
		return self.state


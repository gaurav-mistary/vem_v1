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
	individual = models.ForeignKey('individual',null=True,blank=True,  on_delete=models.CASCADE)
	company = models.ForeignKey('company',null=True,blank=True,  on_delete=models.CASCADE)

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

class machine(modles.Model):
	added_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
	m_name = models.CharField(max_length=60, null=False, blank=False)
	m_image = models.ImageField(upload_to="images/machines/", blank=True, default='defImages/defMachine.jpeg')
	m_upload_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	m_verified = models.BooleanField(default=False, null=True, blank=True)
	m_avail = models.BooleanField(default=False, null=True, blank=True)
	m_subtype = models.CharField(max_length=100, null=True, blank=True, default=None)
	m_location = models.CharField(max_length=1000, null=False, blank=False)
	m_brand = models.CharField(max_length=50, null=True, blank=True)
	m_manufacturing_year = models.CharField(max_length=15, null=True, blank=True)
	m_size = models.DecimalField(max_digits=30, decimal_places=10, default=0, blank=True, null=True)
	m_travel_length = models.DecimalField(max_digits=30, decimal_places=10, default=0, blank=True, null=True)
	m_accuracy = modles.DecimalField(max_digits=10, decimal_places=10, default=0, blank=True, null=True)
	m_spindle_rpm = models.IntegerField(default=0, blank=True, null=True)
	m_tonnage = models.FloatField(default=0, blank=True, null=True)
	m_ra_value = models.DecimalField(max_digits=30, decimal_places=10, default=0, blank=True, null=True)
	m_current_rating = models.DecimalField(max_digits=30, decimal_places=10, default=0, blank=True, null=True)
	m_tie_bar = models.DecimalField(max_digits=30, decimal_places=10, default=0, blank=True, null=True)
	m_shot_weight = models.DecimalField(max_digits=30, decimal_places=10, default=0, blank=True, null=True)

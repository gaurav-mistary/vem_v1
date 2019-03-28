from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()

class register_individual_form(UserCreationForm):
	state = forms.CharField()
	
	class Meta:
		model = User

		fields = ('username','first_name','last_name','email','password1','password2','state')

class register_company_form(UserCreationForm):
	state = forms.CharField(max_length=30, required=True)
	city = forms.CharField(max_length=30, required=True)
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2','state', 'city')

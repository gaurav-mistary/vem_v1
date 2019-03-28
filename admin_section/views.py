from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import datetime
from website.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

def admin_login(request):
	context = []
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if request.GET.get('next', None):
					return HttpResponseRedirect(request.GET['next'])
				return HttpResponseRedirect('/admin_section/home')

		else:
			content = {
			'error': "Provide Valid Credentials !!"
			}
			return render(request, "registration/admin_login.html",content)

	return render(request,'registration/admin_login.html')

def admin_logout(request):
	logout(request)
	return HttpResponseRedirect('/admin_section/login')

def admin_home(request):
	user_count = User.objects.all().count() - 1
	content = {
		'user_count' : user_count,
	}
	return render(request,'admin/admin_home.html', content)

def machine_requested(request):
	return render(request,'admin/admin_machine_requested.html')

def user_authentication_request(request):
	user = User.objects.all()
	individual_verification_list = []
	for user_obj in user:
		if user_obj.is_staff:
			pass
		elif user_obj.is_verified:
			pass
		elif user_obj.is_individual:
			individual_verification_list.append(user_obj)

	for obj in individual_verification_list:
		print(obj.first_name)

	content = {
		'individual_verification_list' : individual_verification_list,
	}
	return render(request,'admin/user_authentication_requested.html', content)
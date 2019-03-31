from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import individual, company, machine, inventory
from .forms import register_individual_form, register_company_form
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

def user_home(request):
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
			'error': "Provide Valid Credentials !!",
			'email_var':'Email is not verified',
			}
			return render(request, "website/index.html",content)
	return render(request,'website/index.html')




def register_company(request):
	if request.method == 'POST':
		print(request.POST)
		form = register_company_form(request.POST)
		if form.is_valid():
			user = form.save()
			
			user.refresh_from_db()
			user.is_active = False
			user.is_company = True
			user.save()
			company.objects.create(user=user, state=form.cleaned_data.get('state'), city=form.cleaned_data.get('city'))
			current_site = get_current_site(request)
			mail_subject = 'Activate your VEM account.'
			message = render_to_string('admin/acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode() ,
				'token':account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
						mail_subject, message, to=[to_email]
			)
			email.send()
			print("valid")
		else:
			print('not valid')
		return HttpResponse('Please confirm your email address to complete the registration')

	else:
		form = register_company_form()
	return render(request, 'website/user_register_company.html', {'form':form})



def register_individual(request):
	if request.method == 'POST':
		form = register_individual_form(request.POST)
		if form.is_valid():

			if form.cleaned_data.get('if_other') == "":
				if_other = None
			else:
				if_other = form.cleaned_data.get('if_other')
			user = form.save()

			
			user.refresh_from_db()
			user.is_active = False
			user.is_individual = True
			user.individual = individual.objects.create(working_industry=form.cleaned_data.get('working_industry'),phone_number = "+91"+form.cleaned_data.get('phone_number'),if_other = if_other)
			user.save()

			current_site = get_current_site(request)
			mail_subject = 'Activate your VEM account.'
			message = render_to_string('admin/acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode() ,
				'token':account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
						mail_subject, message, to=[to_email]
			)
			email.send()
		return HttpResponse('Please confirm your email address to complete the registration')

	else:
		form = register_individual_form()
	return render(request, 'website/user_register_individual.html', {'form':form})

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return redirect('/admin_section/home')
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		return HttpResponse('Activation link is invalid!')

def add_machine(request):
	if request.method == 'POST':
		user = User.objects.get(pk=16)
		machine.objects.create(
			m_added_by = user,
			m_name = request.POST['m_name'],
			m_image = request.POST['m_image'],
			m_subtype = request.POST.get('m_subtype'),
			m_location = request.POST.get('m_location'),
			m_brand = request.POST.get('m_brand'),
			m_manufacturing_year = request.POST['m_manufacturing_year'],
			m_size = request.POST['m_size'],
			m_travel_length = request.POST['m_travel_length'],
			m_accuracy = request.POST['m_accuracy'],
			m_spindle_rpm = request.POST['m_spindle_rpm'],
			m_tonnage = request.POST['m_tonnage'],
			m_ra_value = request.POST['m_ra_value'],
			m_current_rating = request.POST['m_current_rating'],
			m_tie_bar = request.POST['m_tie_bar'],
			m_shot_weight = request.POST['m_shot_weight'],
		)
	return render(request, 'website/add_machine.html')
from django.urls import path, re_path

from . import views


urlpatterns = [
	path('login/', views.admin_login, name='admin_login'),
	path('logout/',views.admin_logout, name = 'logout'),
	path('home/', views.admin_home, name='admin_home'),
	path('machine/requested/', views.machine_requested, name='machine_requested'),
	path('user/authentication/requested', views.user_authentication_request, name='user_authentication_request'),
]

from django.urls import path, re_path

from . import views


urlpatterns = [
	path('', views.user_home, name='user_home'),
	path('register/individual/', views.register_individual, name='register_individual'),
	path('register/company/', views.register_company, name='register_company'),
	path('add/machine/', views.add_machine, name= 'add_machine'),
	re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
]

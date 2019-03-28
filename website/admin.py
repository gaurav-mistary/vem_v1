from django.contrib import admin
from website.models import individual, company
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register([individual,company])
admin.site.register(User, UserAdmin)
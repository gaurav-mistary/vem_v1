from django.contrib import admin
from website.models import individual, company, User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_individual','is_company','is_verified','individual','company',)}),
    )

admin.site.register([individual,company])
admin.site.register(User, MyUserAdmin)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_section/', include('admin_section.urls')),
    path('', include('website.urls')),
]

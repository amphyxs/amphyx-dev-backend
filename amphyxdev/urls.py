from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/personal-info/', include('apps.personal_info.urls')),
]

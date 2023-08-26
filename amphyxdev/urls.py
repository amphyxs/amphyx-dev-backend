from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/personal-info/', include('apps.personal_info.urls')),
    path('api/blog/', include('apps.blog.urls')),
    path('api/projects/', include('apps.projects.urls')),
]

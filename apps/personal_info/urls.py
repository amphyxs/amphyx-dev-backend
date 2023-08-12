from django.urls import path

from apps.personal_info import views

urlpatterns = [
    path('', views.TestView.as_view(), name='index'),
]

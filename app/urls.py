from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from .views import SignUpView

urlpatterns = [
    path('',  TemplateView.as_view(template_name='main.html'), name='main'),
    path('home/', views.home, name='home'),
    path('form/', views.form, name='form'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),

    path('test/', views.test, name='test'),
]
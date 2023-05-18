from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from .views import SignUpView

urlpatterns = [
    path('',  TemplateView.as_view(template_name='LandingPage.html'), name='LandingPage'),
    path('home/', views.home, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('help/', views.help, name='ContactUs'),
    path('about/', views.about, name='About'),
    path('mortgage/', views.mortgage, name='Mortgage'),
    path('details/<int:id>/', views.house_details, name='house_details'),
    path('LandingPage/', views.LandingPage, name='LandingPage'),
]
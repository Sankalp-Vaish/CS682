from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from .views import SignUpView

urlpatterns = [
    path('',  TemplateView.as_view(template_name='LandingPage.html'), name='LandingPage'),
    path('home/', views.home, name='home'),
    path('form/', views.form, name='form'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', views.login_view, name='login_view'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('help/', views.help, name='ContactUs'),
    path('about/', views.about, name='About'),
    path('mortgage/', views.mortgage, name='Mortgage'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('test3/', views.test3, name='test3'),
    path('details/<int:id>/', views.house_details, name='house_details'),
    # path('displayPage', views.displayPage, name='displayPage'),
    path('LandingPage/', views.LandingPage, name='LandingPage'),
    path('main/', views.main, name='main')
]
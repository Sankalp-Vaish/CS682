#This file contains the paths to different pages and which functions to be directed for page rendering. 
from . import views
from django.urls import path


urlpatterns=[
    path("", views.index,  name="prefrences")
]
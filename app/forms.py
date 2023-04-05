from django import forms

class firstform(forms.Form):
    name= forms.CharField(label="Name", max_length=200)
    check= forms.BooleanField()


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Customizedsignupform(UserCreationForm):
    class Meta:
        model= User
        fields=['username', 'email', 'password1', 'password2']  #'__all__'



RENT_CHOICES =(
    ("600", 600),
    ("700", 700),
    ("800", 800),
    ("900", 900),
    ("1000", 1000),
)
  
# creating a form 
class rent_per_unit(forms.Form):
    rent = forms.ChoiceField(choices = RENT_CHOICES)
from django import forms

class firstform(forms.Form):
    name= forms.CharField(label="Name", max_length=200)
    check= forms.BooleanField()

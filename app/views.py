from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import firstform
from . import hello
#from .models import ToDoList

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def home(request):
  
  if request.method== "POST":
    result  = hello.printHello() 
    template = loader.get_template('img.html')
    context = {
    's': result,
    }
    return HttpResponse(template.render(context, request))
  else:
    template = loader.get_template('Home.html')
    return HttpResponse(template.render())

def form(request):
  if request.method== "POST":
    f= firstform(request.POST)
    if f.is_valid():
      n=f.cleaned_data["name"]
      #t=ToDoList(name=n)
      #t.save();
    return HttpResponse("<h1>"+n+"</h1>")
  else:
    f=firstform()
    template = loader.get_template('form.html')
    return HttpResponse(template.render({"form":f}, request))
  
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



def test(request):
  result  = hello.printHello() 
  template = loader.get_template('test.html')
  return HttpResponse(template.render({"r":result}, request))
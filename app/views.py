from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import firstform, Customizedsignupform
from . import hello, test2
from django.contrib.auth.decorators import login_required
#from .models import ToDoList

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def home(request):
  
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
    form_class = Customizedsignupform
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def help(request):
  template = loader.get_template('ContactUs.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())


@login_required(login_url="/accounts/login/")
def mortgage(request):
  template = loader.get_template('mortgage.html')
  return HttpResponse(template.render())

def test(request):
  result  = hello.printHello() 
  template = loader.get_template('test.html')
  return HttpResponse(template.render({"r":result}, request))


def test2(request):
  result  = hello.fetch()
  template = loader.get_template('test2.html')
  return HttpResponse(template.render({"r":result[0]}, request))

@login_required(login_url="/accounts/login/")
def test3(request):
  template = loader.get_template('test3.html')

  if request.method== "POST":
    result  = hello.read_with_prams(request.POST.get('state'), request.POST.get('city'))
    context = {
    "r":result,
    "flag":"True",
    }
    print(request.POST.get('state'))
    print(request.POST.get('city'))
    return HttpResponse(template.render(context, request))
  else:
    print(request)
    cities=hello.read_city()
    states=hello.read_state()
    context = {
    "c":cities,
    "s":states,
    "flag":"False"
    }
    return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from Realtime import settings
from .forms import firstform, Customizedsignupform, rent_per_unit
from . import hello, Calculator
from django.contrib.auth.decorators import login_required
#from .models import ToDoList

from .models import User_details
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def main(request):
  user = request.user
  context = {'user': user}
  template = loader.get_template('main.html')
  return HttpResponse(template.render(context, request))

def home(request):
  user = request.user
  my_location = {'latitude': 37.4224764, 'longitude': -122.0842499}
  context = {'user': user, 'my_location': my_location, 'google_api_key': settings.GOOGLE_MAPS_API_KEY}
  template = loader.get_template('Home.html')
  return HttpResponse(template.render(context, request))

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
  user = request.user
  context = {'user': user}
  template = loader.get_template('ContactUs.html')
  return HttpResponse(template.render(context, request))

def about(request):
  user = request.user
  context = {'user': user}
  template = loader.get_template('about.html')
  return HttpResponse(template.render(context, request))


@login_required(login_url="/accounts/login/")
def mortgage(request):
  template = loader.get_template('mortgage.html')
  exists=User_details.objects.filter(user=request.user).exists()
  details=None
  if exists:
    details=User_details.objects.get(user=request.user)
  
  if request.method== "POST":

    if exists:
      print(request.POST.get("First_Mtg_Interest_Rate"))
      if request.POST.get("First_Mtg_Interest_Rate")!= "":
        details.First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate")
      if request.POST.get("rent")!="":
        details.Average_rent_per_unit= request.POST.get("rent")
      details.save()
    else:
      User_details.objects.create(user=request.user, Average_rent_per_unit=request.POST.get("rent"), First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate"))
    
    id = hello.get_houses_id(request.POST.get('pincode'))
    result = hello.get_house_list(id)
    #print(result)
    if result==[]:
      context = {
      "z":"No houses found",
      "flag":"True",
      }
      
    else:
      l=hello.get_dict(result)
      context = {
      "r":l,
      "z":"",
      "flag":"True",
      "rent": rent_per_unit(),
      "details":details
      }
    return HttpResponse(template.render(context, request))
  else:
    context = {
    "flag":"False",
    "rent": rent_per_unit(),
    "details":details
    }
    return HttpResponse(template.render(context, request))


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
  exists=User_details.objects.filter(user=request.user).exists()
  details=None
  if exists:
    details=User_details.objects.get(user=request.user)
  if request.method== "POST":
    if exists:
      print(request.POST.get("First_Mtg_Interest_Rate"))
      if request.POST.get("First_Mtg_Interest_Rate")!= "":
        details.First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate")
      if request.POST.get("rent")!="":
        details.Average_rent_per_unit= request.POST.get("rent")
      details.save()
    else:
      User_details.objects.create(user=request.user, Average_rent_per_unit=request.POST.get("rent"), First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate"))
    result  = hello.read_with_prams(request.POST.get('state'), request.POST.get('city'), request.POST.get('street_name'))
    #print(details.Average_rent_per_unit, details.First_Mtg_Interest_Rate)
    l=hello.get_dict(result)
    context = {
    "r":l,
    "flag":"True",
    "details":details
    }
    return HttpResponse(template.render(context, request))
  else:
    print(request)
    cities=hello.read_city()
    states=hello.read_state()
    street_name=hello.read_street_name()
    context = {
    "c":cities,
    "s":states,
    "street_name":street_name,
    "flag":"False",
    "rent": rent_per_unit(),
    "details":details
    }
    return HttpResponse(template.render(context, request))
  

def house_details(request, id):
  template = loader.get_template('house_details.html')
  l=hello.get_id_list()
  house=None
  for i in l:
    if int(i)==int(id):
      #print("Yes")
      house=hello.get_details(id)
  if house==None:
    #print("No")
    house=hello.get_details_by_pin(id)
  details=User_details.objects.get(user=request.user)
  print(details.First_Mtg_Interest_Rate)
  result=Calculator.calculator(house["list_price"], house["unit"], house["tax"], house["insurance_rate"], details.First_Mtg_Interest_Rate, details.Average_rent_per_unit)
  context = {
    "flag":"True",
    "y" : id,
    "house" : house,
    "calc" : result
    }
  return HttpResponse(template.render(context, request))


def displayPage(request):
  template = loader.get_template('displayPage.html')
  result=Calculator.calculator()
  context = {
    "calc" : result
    }
  return HttpResponse(template.render(context, request))



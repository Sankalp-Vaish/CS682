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

#from django_google_maps import fields as map_fields
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyB-fRkRcT8UPA8u_70e8ah3LOHWdt5bkak')

def main(request):
  user = request.user
  context = {'user': user}
  template = loader.get_template('main.html')
  return HttpResponse(template.render(context, request))

def home(request):
  user = request.user
  my_location = {'latitude': 37.4224764, 'longitude': -122.0842499}
  geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
  location = geocode_result[0]['geometry']['location']
  latitude = location['lat']
  longitude = location['lng']
  context = {'user': user, 'my_location': my_location, 'geocode_result': geocode_result, 'google_api_key': settings.GOOGLE_MAPS_API_KEY}
  # address = map_fields.AddressField(max_length=200)
  # geolocation = map_fields.GeoLocationField(max_length=100)
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
  if request.method== "POST":
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
      }
    return HttpResponse(template.render(context, request))
  else:
    context = {
    "flag":"False"
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

  if request.method== "POST":
    result  = hello.read_with_prams(request.POST.get('state'), request.POST.get('city'), request.POST.get('street_name'))
    User_details.First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate")
    User_details.Average_rent_per_unit= request.POST.get("rent")
    
    print(User_details.Average_rent_per_unit, User_details.First_Mtg_Interest_Rate)
    l=hello.get_dict(result)
    context = {
    "r":l,
    "flag":"True",
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
    "rent": rent_per_unit()
    }
    return HttpResponse(template.render(context, request))
  

def house_details(request, id):
  template = loader.get_template('house_details.html')
  house=hello.get_details(id)
  result=Calculator.calculator(house["list_price"], house["unit"], house["tax"], house["insurance_rate"], User_details.First_Mtg_Interest_Rate, User_details.Average_rent_per_unit)
  context = {
    "flag":"True",
    "y" : id,
    "house" : house,
    "calc" : result
    }
  return HttpResponse(template.render(context, request))


def displayPage(request):
  template = loader.get_template('displayPage.html')
  # result=Calculator.calculator()
  # context = {
  #   "calc" : result
  #   }
  return HttpResponse(template.render(None, request))



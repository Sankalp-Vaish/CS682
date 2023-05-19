"""
The controller contains logic that updates the model and/or view in response to input from the users of the app.

These functions have which pages to be rendered and with what context. 
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from Realtime import settings
from .forms import Customizedsignupform, rent_per_unit
from . import fetch, Calculator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import User_details, favourites
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from geopy.geocoders import Nominatim
import threading


#Main Page Or Landing Page
def LandingPage(request):
  user = request.user
  context = {'user': user}
  template = loader.get_template('LandingPage.html')
  return HttpResponse(template.render(context, request))

#Home Page
def home(request):
  user = request.user
  if request.method== "POST":
    id= request.POST.get("prop_id")
    if favourites.objects.filter(user=user, property_id= id).exists():
      fav=favourites.objects.filter(user=user, property_id= id)
      fav.delete()

  exists=favourites.objects.filter(user=request.user).exists()
  if exists:
    fav=favourites.objects.all().values()
    context = {'user': user,
            'fav': fav,
            }
  else:
    context = {'user': user,
            }
  template = loader.get_template('Home.html')
  return HttpResponse(template.render(context, request))

#Signup Page  
class SignUpView(generic.CreateView):
    form_class = Customizedsignupform
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

#Contact Us Page
def help(request):
  user = request.user
  context = {'user': user}
  template = loader.get_template('ContactUs.html')
  return HttpResponse(template.render(context, request))

#About Page
def about(request):
  user = request.user
  context = {'user': user}
  template = loader.get_template('about.html')
  return HttpResponse(template.render(context, request))

#Propert Search Page
@login_required(login_url="/accounts/login/")
def mortgage(request):
  template = loader.get_template('mortgage.html')
  exists=User_details.objects.filter(user=request.user).exists()
  details=None
  if exists:
    details=User_details.objects.get(user=request.user)
  
  if request.method== "POST":

    if "address" in request.POST:

      add=request.POST.get("address")
      form=rent_per_unit()
      geolocator = Nominatim(user_agent="geoapi")
      try:
        location = geolocator.geocode(add, timeout=10) 
        data = location.raw
        loc_data = data['display_name'].split()
        pin=(loc_data[-3][:-1])
      except:
        print("Error in Extrancting Pincode")
    else:
      if exists:
        if request.POST.get("First_Mtg_Interest_Rate")!= "":
          details.First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate")
        if request.POST.get("rent")!="":
          form=rent_per_unit(initial={"rent": [str(request.POST.get("rent")), request.POST.get("rent")]})
          details.Average_rent_per_unit= request.POST.get("rent")
        details.save()
      else:
        form=rent_per_unit()
        User_details.objects.create(user=request.user, Average_rent_per_unit=request.POST.get("rent"), First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate"))   
      pin=request.POST.get('pincode')
    
    id = fetch.get_houses_id(pin)
    if id==None:
      context = {
      "z":"No houses found",
      "flag":"True",
      }

    else:
      lock = threading.Lock()
      t=[]
      c=0
      for i in range(0,5,2):#29
        t.append(threading.Thread(target=fetch.get_house_list, name='t'+str(c+1), args=(id[i:(i+2)],lock,)))
        t[c].start()
        c=c+1
      for i in range(3):#15
        t[i].join()

      result = fetch.get_prop_list()
      # print("res",result)
      l=fetch.get_dict(result, request)
      context = {
      "len":len(result),
      "r":l,
      "z":"",
      "flag":"True",
      "rent": form,
      "details":details,
      "pin":pin
      }
    return HttpResponse(template.render(context, request))
  else:
    context = {
    "flag":"False",
    "rent": rent_per_unit(),
    "details":details
    }
    return HttpResponse(template.render(context, request))

# House Detail Page
def house_details(request, id):
  template = loader.get_template('house_details.html')
  flag=False
  user = request.user
  if favourites.objects.filter(user=user, property_id= id).exists():
    flag=True

  # If user Clicks on Fav Icon only then this if condition will execute  
  if request.method== "POST":   
    if favourites.objects.filter(user=user, property_id= id).exists():  #If for remove from Favourites List
      fav=favourites.objects.filter(user=user, property_id= id)
      fav.delete()
      flag=False
    
    else:             # Add to Favourites List
      house=None
      if house==None:
        house=fetch.get_details_by_pin(id, request)
      fav= favourites(user=request.user, city= house["city"],
      status = house["status"],
      year_built = house["year_built"],
      baths = house["baths"],
      beds = house["beds"],
      stories = house["stories"],
      list_price = house["list_price"],
      unit = house["unit"],
      postal_code = house["postal_code"],
      street_name = house["street_name"],
      lat = house["lat"],
      lon = house["lon"],
      link = house["link"][0]["href"] ,
      property_id = house["property_id"],
      tax = house["tax"],
      insurance_rate = house["insurance_rate"],
      Cashflow_per_unit_per_month= house["cash"],
      Cash_On_Cash_ROI= house["Cash_On_Cash_ROI"],
      fav_toggle=True)
      fav.save()
      flag=True


  house=None
  if house==None:
    house=fetch.get_details_by_pin(id, request)
  details=User_details.objects.get(user=request.user)
  #print(details.First_Mtg_Interest_Rate)
  result=Calculator.calculator(request, house["list_price"], house["unit"], house["tax"], house["insurance_rate"], details.First_Mtg_Interest_Rate, details.Average_rent_per_unit)
  context = {
    "flag":"True",
    "y" : id,
    "house" : house,
    "calc" : result,
    "bool" : flag
    }
  return HttpResponse(template.render(context, request))

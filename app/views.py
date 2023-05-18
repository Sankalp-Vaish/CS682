from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from Realtime import settings
from .forms import Customizedsignupform, rent_per_unit
from . import hello, Calculator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import User_details, favourites
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from UserPrefrences.models import UserPref
from geopy.geocoders import Nominatim
import threading



def LandingPage(request):
  user = request.user
  context = {'user': user}
  template = loader.get_template('LandingPage.html')
  return HttpResponse(template.render(context, request))

def home(request):

  user = request.user
  pref=UserPref.objects.get(user=request.user)
  if request.method== "POST":
    id= request.POST.get("prop_id")
    print(id)
    if favourites.objects.filter(user=user, property_id= id).exists():
      print("before delete")
      fav=favourites.objects.filter(user=user, property_id= id)
      fav.delete()
      print("after delete")

  exists=favourites.objects.filter(user=request.user).exists()
  if exists:
    fav=favourites.objects.all().values()
    context = {'user': user,
            'pref': pref.currency,
            'fav': fav,
            }
  else:
    context = {'user': user,
            'pref': pref.currency,
            }
  template = loader.get_template('Home.html')
  return HttpResponse(template.render(context, request))

  
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

    if "address" in request.POST:
      print("Gotcha")
      add=request.POST.get("address")
      form=rent_per_unit()
      print(add)
      geolocator = Nominatim(user_agent="geoapi")
      try:
        location = geolocator.geocode(add, timeout=10) 
        data = location.raw
        loc_data = data['display_name'].split()
        print(loc_data[-3][:-1])
        pin=(loc_data[-3][:-1])
      except:
        print("some error")
    else:
      if exists:
        print(request.POST.get("First_Mtg_Interest_Rate"))
        if request.POST.get("First_Mtg_Interest_Rate")!= "":
          details.First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate")
        if request.POST.get("rent")!="":
          form=rent_per_unit(initial={"rent": [str(request.POST.get("rent")), request.POST.get("rent")]})
          details.Average_rent_per_unit= request.POST.get("rent")
        details.save()
      else:
        User_details.objects.create(user=request.user, Average_rent_per_unit=request.POST.get("rent"), First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate"))   
      pin=request.POST.get('pincode')
    
    id = hello.get_houses_id(pin)
    #print(id)
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
        t.append(threading.Thread(target=hello.get_house_list, name='t'+str(c+1), args=(id[i:(i+2)],lock,)))
        t[c].start()
        c=c+1
        print(c)
        # if i ==2:
        #   break
      for i in range(3):#15
        t[i].join()

      result = hello.get_prop_list()
      print("res",result)
      l=hello.get_dict(result, request)
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


  

def house_details(request, id):
  template = loader.get_template('house_details.html')
  flag=False
  user = request.user
  if favourites.objects.filter(user=user, property_id= id).exists():
    flag=True
  if request.method== "POST":
    if favourites.objects.filter(user=user, property_id= id).exists():
      fav=favourites.objects.filter(user=user, property_id= id)
      fav.delete()
      flag=False
    else:

      house=None
      if house==None:
        house=hello.get_details_by_pin(id, request)
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
      print(house["cash"])
      #fav=favourites.objects.get(user=request.user)
      fav.save()
      flag=True
      print(house["link"])
      print("fav", fav.link)

  house=None
  if house==None:
    house=hello.get_details_by_pin(id, request)
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



def main(request):
  user = request.user
  my_location = {'latitude': 37.4224764, 'longitude': -122.0842499}
  context = {'user': user,
             'my_location': my_location,
    'google_api_key': settings.GOOGLE_MAPS_API_KEY}
  template = loader.get_template('main.html')
  return HttpResponse(template.render(context, request))


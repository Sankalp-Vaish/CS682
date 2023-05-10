from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from Realtime import settings
from .forms import firstform, Customizedsignupform, rent_per_unit
from . import hello, Calculator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
#from .models import ToDoList

from .models import User_details, favourites
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from UserPrefrences.models import UserPref#, Property_Info, Environmentals, Financing, Income, Operating_Expenses, Pests, Cash_requirements
from geopy.geocoders import Nominatim
import threading



def LandingPage(request):
  user = request.user
  context = {'user': user}
  template = loader.get_template('LandingPage.html')
  return HttpResponse(template.render(context, request))

def home(request):
  # user = request.user
  # if request.method== "POST":
  #   add=request.POST.get("address")
  #   #print(add)
  #   geolocator = Nominatim(user_agent="geoapi")
  #   try:
  #     location = geolocator.geocode(add, timeout=10) 
  #     data = location.raw
  #     loc_data = data['display_name'].split()
  #     print(loc_data[-3][:-1])
  #   except:
  #     print("some error")
  # #else:
  # my_location = {'latitude': 37.4224764, 'longitude': -122.0842499}
  # context = {'user': user, 'my_location': my_location, 'google_api_key': settings.GOOGLE_MAPS_API_KEY}
  user = request.user
  pref=UserPref.objects.get(user=request.user)
  #flag=False
  #print("vv",pref.currency)
  if request.method== "POST":
    id= request.POST.get("prop_id")
    print(id)
    if favourites.objects.filter(user=user, property_id= id).exists():
      print("before delete")
      fav=favourites.objects.filter(user=user, property_id= id)
      fav.delete()
      print("after delete")
      #flag=False

  exists=favourites.objects.filter(user=request.user).exists()
  if exists:
    #fav=favourites.objects.get(user=request.user)
    fav=favourites.objects.all().values()
    #flag=True
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

def login_view(request):
  if request.method=="POST":
    username = request.POST["Username"]
    password = request.POST["Password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect("home")
    else:
      messages.success(request, ("There was an Error"))
      return redirect("login_view")
  else:
    return render(request, "registration\login.html")

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
      for i in range(0,3,2):#29
        t.append(threading.Thread(target=hello.get_house_list, name='t'+str(c+1), args=(id[i:(i+2)],lock,)))
        t[c].start()
        c=c+1
        print(c)
        # if i ==2:
        #   break
      for i in range(2):#15
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


def test(request):
  result  = None#hello.printHello() 
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
    if "address" in request.POST:
      print("Gotcha")
      add=request.POST.get("address")
      print(add)
      geolocator = Nominatim(user_agent="geoapi")
      try:
        location = geolocator.geocode(add, timeout=10) 
        data = location.raw
        loc_data = data['display_name'].split()
        print(loc_data[-3][:-1])
        pin=int(loc_data[-3][:-1])
      except:
        print("some error")
    else:
      if exists:
        print(request.POST.get("First_Mtg_Interest_Rate"))
        if request.POST.get("First_Mtg_Interest_Rate")!= "":
          details.First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate")
        if request.POST.get("rent")!="":
          details.Average_rent_per_unit= request.POST.get("rent")
          form=rent_per_unit(initial={"rent": [str(request.POST.get("rent")), request.POST.get("rent")]})
          print(form)
          #print()
          # rent_per_unit.rent.initial= request.POST.get("rent")
        details.save()
      else:
        User_details.objects.create(user=request.user, Average_rent_per_unit=request.POST.get("rent"), First_Mtg_Interest_Rate=request.POST.get("First_Mtg_Interest_Rate"))
    result  = hello.read_with_prams(request.POST.get('state'), request.POST.get('city'), request.POST.get('street_name'))
    #print(details.Average_rent_per_unit, details.First_Mtg_Interest_Rate)
    l=hello.get_dict(result, request)
    # cash=[]
    # for house in l:
    #   calc=Calculator.calculator(house["list_price"], house["unit"], house["tax"], house["insurance_rate"], details.First_Mtg_Interest_Rate, details.Average_rent_per_unit)
    #   cash.append(calc["Cashflow_per_unit_per_month"])
    my_location = {'latitude': 37.4224764, 'longitude': -122.0842499}
    user = request.user
    context = {
    "r":l,
    "flag":"True",
    "details":details,
    "f":form,
    "rent": rent_per_unit(),
    'user': user,
    'my_location': my_location,
    'google_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return HttpResponse(template.render(context, request))
  else:
    pref=UserPref.objects.get(user=request.user)
    print("vv",pref.currency)
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
  flag=False
  user = request.user
  if favourites.objects.filter(user=user, property_id= id).exists():
    flag=True
  if request.method== "POST":
    
    #favourites.objects.filter(user=user, property_id= id).delete()
    if favourites.objects.filter(user=user, property_id= id).exists():
      #print("before- ", favourites.objects.filter(user=user, property_id= id).exists)
      fav=favourites.objects.filter(user=user, property_id= id)
      fav.delete()
      flag=False
      #print("after- ",favourites.objects.filter(user=user, property_id= id).exists)
      #fav.save()
    else:
    #print( "filter", favourites.objects.filter(user=user, property_id= 2896525175))
    #if True:#request.method == "POST":
      house=None
      l=hello.get_id_list()
      for i in l:
        if int(i)==int(id):
          #print("Yes")
          house=hello.get_details(id, request)
      if house==None:
        house=hello.get_details_by_pin(id, request)
      # exists=favourites.objects.filter(user=request.user).exists()
      # if exists:
      #   #fav=favourites.objects.get(user=request.user)
      #   pass
      # else:
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
  #else:
  #print("before",id)
  l=hello.get_id_list()
  house=None
  for i in l:
    if int(i)==int(id):
      #print("Yes")
      house=hello.get_details(id, request)
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


def displayPage(request):
  template = loader.get_template('displayPage.html')
  result=Calculator.calculator(request)
  context = {
    "calc" : result
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


# def fav(request, id):
#   user = request.user
#   #favourites.objects.filter(user=user, property_id= id).delete()
#   if favourites.objects.filter(user=user, property_id= id).exists():
#     print("before- ", favourites.objects.filter(user=user, property_id= id).exists)
#     fav=favourites.objects.filter(user=user, property_id= id)
#     fav.delete()
#     print("after- ",favourites.objects.filter(user=user, property_id= id).exists)
#     #fav.save()
#   else:
#   #print( "filter", favourites.objects.filter(user=user, property_id= 2896525175))
#   #if True:#request.method == "POST":
#     house=None
#     l=hello.get_id_list()
#     for i in l:
#       if int(i)==int(id):
#         #print("Yes")
#         house=hello.get_details(id)
#     if house==None:
#       house=hello.get_details_by_pin(id)
#     # exists=favourites.objects.filter(user=request.user).exists()
#     # if exists:
#     #   #fav=favourites.objects.get(user=request.user)
#     #   pass
#     # else:
#     fav= favourites(user=request.user, city= house["city"],
#     status = house["status"],
#     year_built = house["year_built"],
#     baths = house["baths"],
#     beds = house["beds"],
#     stories = house["stories"],
#     list_price = house["list_price"],
#     unit = house["unit"],
#     postal_code = house["postal_code"],
#     street_name = house["street_name"],
#     lat = house["lat"],
#     lon = house["lon"],
#     link = house["link"],
#     property_id = house["property_id"],
#     tax = house["tax"],
#     insurance_rate = house["insurance_rate"],
#     fav_toggle=True)
#     #fav=favourites.objects.get(user=request.user)
#     fav.save()
#   #print("ppp")
#   #print("lp", fav.property_id)
    
#   return HttpResponseRedirect(request.path_info)#house_details, id=id)#request.path_info)
    
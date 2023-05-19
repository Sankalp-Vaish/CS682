import requests
from urllib.request import urlopen
import time
import plotly.express as px
import plotly
from . import Calculator
from .models import User_details, favourites

First_Mtg_Interest_Rate=0.001

#function to get property id list
def get_houses_id(pincode):
    url = "https://realty-in-us.p.rapidapi.com/properties/v3/list"

    payload = {
        "limit": 200,
        "offset": 0,
        "postal_code": pincode,
        "status": ["for_sale", "ready_to_build"],
        "sort": {
            "direction": "desc",
            "field": "list_date"
        }
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "bb9ac65a8amshe62c50a495c4953p1d9b10jsn4ff18233cf14",
        "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
    }

    response_list = requests.request("POST", url, json=payload, headers=headers)

    property_id=[]
    d=dict(response_list.json())
    for property in d['data']['home_search']['results']:
        property_id.append(property['property_id'])
    
    return property_id


prop_list=[]
c=0
#Funtion to get house list from house id's.
def get_house_list(property_id, lock):
    url = "https://realty-in-us.p.rapidapi.com/properties/v3/detail"
    global prop_list
    prop_list=[]
    global c
    for i in property_id:
        
        
        querystring = {"property_id":i}

        headers = {
            "X-RapidAPI-Key": "bb9ac65a8amshe62c50a495c4953p1d9b10jsn4ff18233cf14",
            "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
        }

        #print(response.text)
        lock.acquire()
        c=c+1
        if c==4:
            c=0
            time.sleep(1)
        response = requests.request("GET", url, headers=headers, params=querystring)
        prop_list.append(response.json())
        lock.release()

#Getter Function for Property List
def get_prop_list():
    return prop_list

#Function to get all the details for a particular property
def get_details_by_pin(id, request):
    details=User_details.objects.get(user=request.user)
    r=dict()
    url = "https://realty-in-us.p.rapidapi.com/properties/v3/detail"

    querystring = {"property_id":id}

    headers = {
        "X-RapidAPI-Key": "bb9ac65a8amshe62c50a495c4953p1d9b10jsn4ff18233cf14",
        "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    house=response.json()
    #print("in")
    r["city"]=house["data"]["home"]["location"]["address"]["city"] 
    r["status"]=house["data"]["home"]["status"]
    r["year_built"]=house["data"]["home"]["description"]["year_built"]
    r["baths"]=house["data"]["home"]["description"]["baths"]
    r["beds"]=house["data"]["home"]["description"]["beds"]
    r["stories"]=house["data"]["home"]["description"]["stories"]
    r["list_price"]=house["data"]["home"]["list_price"]
    r["unit"]=house["data"]['home']['description']['units']
    r["postal_code"]=house["data"]["home"]["location"]["address"]["postal_code"]
    r["street_name"]=house["data"]["home"]["location"]["address"]["street_name"]
    if house["data"]["home"]["photos"]:
        r["link"]=house["data"]["home"]["photos"]
    if house["data"]['home']["location"]["address"]["coordinate"]:
        r["lat"]= house["data"]['home']["location"]["address"]["coordinate"]["lat"]
        r["lon"]= house["data"]['home']["location"]["address"]["coordinate"]["lon"]
    r["property_id"]=house["data"]["home"]["property_id"]
    if house["data"]['home']['tax_history']:
        r["tax"]=house["data"]['home']['tax_history'][0]["tax"]
    else:
        r["tax"]=None
    r["insurance_rate"]=house["data"]['home']['mortgage']["insurance_rate"]
    r["First_Mtg_Interest_Rate"]=First_Mtg_Interest_Rate
    calc=Calculator.calculator(request, r["list_price"], r["unit"], r["tax"], r["insurance_rate"], details.First_Mtg_Interest_Rate, details.Average_rent_per_unit)
    r["cash"]=int(float(calc["Cashflow_per_unit_per_month"]))
    r["Cash_On_Cash_ROI"]=int(float(calc["Cash_On_Cash_ROI"]))
    print(r["tax"])
    #print(r["city"])
    return r

#Function to extract details in a Format
def get_dict(result, request):
    l=[]
    details=User_details.objects.get(user=request.user)
    r=dict()
    for house in result:
      r["city"]=house["data"]["home"]["location"]["address"]["city"] 
      r["list_price"]=house["data"]["home"]["list_price"]
      r["postal_code"]=house["data"]["home"]["location"]["address"]["postal_code"]
      r["street_name"]=house["data"]["home"]["location"]["address"]["street_name"]
      r["year_built"]=house["data"]["home"]["description"]["year_built"]
      r["baths"]=house["data"]["home"]["description"]["baths"]
      r["beds"]=house["data"]["home"]["description"]["beds"]
      r["stories"]=house["data"]["home"]["description"]["stories"]
      r["unit"]=house["data"]['home']['description']['units']
      if house["data"]["home"]["photos"]:
        r["link"]=house["data"]["home"]["photos"][0]["href"] 
      r["property_id"]=house["data"]["home"]["property_id"]
      if house["data"]['home']["location"]["address"]["coordinate"]:
        r["lat"]= house["data"]['home']["location"]["address"]["coordinate"]["lat"]
        r["lon"]= house["data"]['home']["location"]["address"]["coordinate"]["lon"]
        r["latitude"]=house["data"]["home"]["location"]["address"]["coordinate"]["lat"]
        r["longitude"]=house["data"]["home"]["location"]["address"]["coordinate"]["lon"]
      r["insurance_rate"]=house["data"]['home']['mortgage']["insurance_rate"]
      if favourites.objects.filter(user=request.user, property_id= r["property_id"]).exists():
          r["bool"]=True
      else:
          r["bool"]=False
      if house["data"]['home']['tax_history']:
        r["tax"]=house["data"]['home']['tax_history'][0]["tax"]
      else:
        r["tax"]=None
      calc=Calculator.calculator(request, r["list_price"], r["unit"], r["tax"], r["insurance_rate"], details.First_Mtg_Interest_Rate, details.Average_rent_per_unit)
      r["cash"]=int(float(calc["Cashflow_per_unit_per_month"]))
      r["Cash_On_Cash_ROI"]=int(float(calc["Cash_On_Cash_ROI"]))
      l.append(r)
      r=dict()
    
    return l
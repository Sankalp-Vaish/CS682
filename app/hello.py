import requests
from urllib.request import urlopen
from six import BytesIO #Used internally by PIL 
from PIL import Image, ImageDraw, ImageFont
import json
import time
import plotly.express as px
import plotly
from . import Calculator
from .models import User_details

First_Mtg_Interest_Rate=0.001
def printHello(): 
    url = "https://realty-in-us.p.rapidapi.com/properties/v3/detail"

    querystring = {"property_id":"2186526216"}

    headers = {
        "X-RapidAPI-Key": "ea8552e940msh3f14dc78146fae7p16308ejsn1bedafc35b28",
        "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)
    d=dict(response.json())
    path=d['hugePhotos'][0]['url']
    """response = urlopen(path)
    image_data = response.read()
    image_data = BytesIO(image_data)
    image = Image.open(image_data)"""

    #return d["address"]["city"]
    return path


def read_city(): 
    
    d=json.load(open(r"app/data_file.json"))
    city=[]
    for house in d:
        city.append(house["data"]["home"]["location"]["address"]['city'])
    return set(city)

def read_state(): 
    
    d=json.load(open(r"app/data_file.json"))
    state=[]
    for house in d:
        state.append(house["data"]["home"]["location"]["address"]['state'])
    return set(state)

def read_street_name(): 
    
    d=json.load(open(r"app/data_file.json"))
    street_name=[]
    for house in d:
        street_name.append(house["data"]["home"]["location"]["address"]['street_name'])
    return set(street_name)

def read_with_prams(search_state, search_city, street_name): 
    
    d=json.load(open(r"app/data_file.json"))

    house_list=[]
    for house in d:
        if house["data"]["home"]["location"]["address"]["state"]==search_state:
            #print(search_city,  house["data"]["home"]["location"]["address"]["city"])
            if house["data"]["home"]["location"]["address"]["city"]=="Los Angeles":
                #print("city in")
                if house["data"]["home"]["location"]["address"]["street_name"]==street_name:
                    house_list.append(house)
    return house_list


def fetch():
    
    house_list=[{'bathrooms': 1.0,
    'bedrooms': 2.0,
    'zpid': 7600516}]
    
    return house_list


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
        "X-RapidAPI-Key": "26ae97eb9emshad0cd9d923c9392p1e08b4jsna0070d71438f",
        "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
    }

    response_list = requests.request("POST", url, json=payload, headers=headers)

    property_id=[]
    d=dict(response_list.json())
    for property in d['data']['home_search']['results']:
        property_id.append(property['property_id'])
    
    return property_id


prop_list=[]
def get_house_list(property_id, lock):
    url = "https://realty-in-us.p.rapidapi.com/properties/v3/detail"
    global prop_list
    c=0
    for i in property_id:
        """c=c+1
        if c==4:
            c=0
            time.sleep(2)"""
        
        querystring = {"property_id":i}

        headers = {
            "X-RapidAPI-Key": "26ae97eb9emshad0cd9d923c9392p1e08b4jsna0070d71438f",
            "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        #print(response.text)
        lock.acquire()
        prop_list.append(response.json())
        lock.release()

def get_prop_list():
    return prop_list

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
      r["link"]=house["data"]["home"]["photos"][0]["href"] 
      r["property_id"]=house["data"]["home"]["property_id"]
      r["lat"]= house["data"]['home']["location"]["address"]["coordinate"]["lat"]
      r["lon"]= house["data"]['home']["location"]["address"]["coordinate"]["lon"]
      r["latitude"]=house["data"]["home"]["location"]["address"]["coordinate"]["lat"]
      r["longitude"]=house["data"]["home"]["location"]["address"]["coordinate"]["lon"]
      r["insurance_rate"]=house["data"]['home']['mortgage']["insurance_rate"]
      if house["data"]['home']['tax_history']:
        r["tax"]=house["data"]['home']['tax_history'][0]["tax"]
      else:
        r["tax"]=None
      calc=Calculator.calculator(request, r["list_price"], r["unit"], r["tax"], r["insurance_rate"], details.First_Mtg_Interest_Rate, details.Average_rent_per_unit)
      r["cash"]=int(float(calc["Cashflow_per_unit_per_month"]))
      l.append(r)
      r=dict()
    
    return l


def get_details(id):
    r=dict()
    d=json.load(open(r"app/data_file.json"))
    for house in d:
        #print("house ", type(house["data"]["home"]["property_id"]))
        if house["data"]["home"]["property_id"]==str(id):
            print("in")
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
            r["lat"]= house["data"]['home']["location"]["address"]["coordinate"]["lat"]
            r["lon"]= house["data"]['home']["location"]["address"]["coordinate"]["lon"]
            r["link"]=house["data"]["home"]["photos"] 
            r["property_id"]=house["data"]["home"]["property_id"]
            if house["data"]['home']['tax_history']:
                r["tax"]=house["data"]['home']['tax_history'][0]["tax"]
            else:
                r["tax"]=None
            r["insurance_rate"]=house["data"]['home']['mortgage']["insurance_rate"]
            r["First_Mtg_Interest_Rate"]=First_Mtg_Interest_Rate
            print(r["tax"])
            y=[]
            t=[]
            if house["data"]["home"]["tax_history"]:
                for i in house["data"]["home"]["tax_history"]:
                    t.append(i["tax"])
                    y.append(i["year"])
                fig=px.line(x=y, y=t, labels={ "x": "year", "y":"tax($)"})
                #plotly.offline.plot(fig, filename=r'images/fig1.jpeg')
                fig.write_image(r"app/static/images/tax.jpeg")
            #print(r["city"])
    return r


def get_details_by_pin(id):
    r=dict()
    url = "https://realty-in-us.p.rapidapi.com/properties/v3/detail"

    querystring = {"property_id":id}

    headers = {
        "X-RapidAPI-Key": "ea8552e940msh3f14dc78146fae7p16308ejsn1bedafc35b28",
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
    r["link"]=house["data"]["home"]["photos"]
    r["lat"]= house["data"]['home']["location"]["address"]["coordinate"]["lat"]
    r["lon"]= house["data"]['home']["location"]["address"]["coordinate"]["lon"]
    r["property_id"]=house["data"]["home"]["property_id"]
    if house["data"]['home']['tax_history']:
        r["tax"]=house["data"]['home']['tax_history'][0]["tax"]
    else:
        r["tax"]=None
    r["insurance_rate"]=house["data"]['home']['mortgage']["insurance_rate"]
    r["First_Mtg_Interest_Rate"]=First_Mtg_Interest_Rate
    print(r["tax"])
    #print(r["city"])
    return r


def get_id_list():
    d=json.load(open(r"app/data_file.json"))
    l=[]
    for i in d:
        l.append(i["data"]["home"]["property_id"])
    return l
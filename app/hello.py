import requests
from urllib.request import urlopen
from six import BytesIO #Used internally by PIL 
from PIL import Image, ImageDraw, ImageFont
import json
import time


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
    
    d=json.load(open(r"app\data_file.json"))
    city=[]
    for house in d:
        city.append(house["data"]["home"]["location"]["address"]['city'])
    return set(city)

def read_state(): 
    
    d=json.load(open(r"app\data_file.json"))
    state=[]
    for house in d:
        state.append(house["data"]["home"]["location"]["address"]['state'])
    return set(state)

def read_street_name(): 
    
    d=json.load(open(r"app\data_file.json"))
    street_name=[]
    for house in d:
        street_name.append(house["data"]["home"]["location"]["address"]['street_name'])
    return set(street_name)

def read_with_prams(search_state, search_city, street_name): 
    
    d=json.load(open(r"app\data_file.json"))

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
        "X-RapidAPI-Key": "ea8552e940msh3f14dc78146fae7p16308ejsn1bedafc35b28",
        "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
    }

    response_list = requests.request("POST", url, json=payload, headers=headers)

    property_id=[]
    d=dict(response_list.json())
    for property in d['data']['home_search']['results']:
        property_id.append(property['property_id'])
    
    return property_id

def get_house_list(property_id):
    url = "https://realty-in-us.p.rapidapi.com/properties/v3/detail"
    prop_list=[]
    c=0
    for i in property_id[:2]:
        """c=c+1
        if c==4:
            c=0
            time.sleep(2)"""
        
        querystring = {"property_id":i}

        headers = {
            "X-RapidAPI-Key": "2e7b06639bmshe0265e0dddf1f4fp17f3aajsn65bb8c0da710",
            "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
        prop_list.append(response.json())

    return prop_list
 
def get_dict(result):
    l=[]
    r=dict()
    for house in result:
      r["city"]=house["data"]["home"]["location"]["address"]["city"] 
      r["status"]=house["data"]["home"]["status"]
      r["year_built"]=house["data"]["home"]["description"]["year_built"]
      r["baths"]=house["data"]["home"]["description"]["baths"]
      r["beds"]=house["data"]["home"]["description"]["beds"]
      r["stories"]=house["data"]["home"]["description"]["stories"]
      r["list_price"]=house["data"]["home"]["list_price"]
      r["unit"]=house["data"]["home"]["location"]["address"]["unit"] 
      r["postal_code"]=house["data"]["home"]["location"]["address"]["postal_code"]
      r["street_name"]=house["data"]["home"]["location"]["address"]["street_name"]
      r["link"]=house["data"]["home"]["photos"][0]["href"] 
      l.append(r)
      r=dict()
    
    return l
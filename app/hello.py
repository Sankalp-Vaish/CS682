import requests
from urllib.request import urlopen
from six import BytesIO #Used internally by PIL 
from PIL import Image, ImageDraw, ImageFont
import json


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

def read_with_prams(search_state, search_city): 
    
    d=json.load(open(r"app\data_file.json"))

    house_list=[]
    for house in d:
        if house["data"]["home"]["location"]["address"]["state"]==search_state:
            #print(search_city,  house["data"]["home"]["location"]["address"]["city"])
            if house["data"]["home"]["location"]["address"]["city"]=="Los Angeles":
                #print("city in")
                house_list.append(house)
    return house_list


def fetch():
    
    house_list=[{'bathrooms': 1.0,
    'bedrooms': 2.0,
    'zpid': 7600516}]
    
    return house_list
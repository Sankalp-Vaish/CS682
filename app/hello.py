import requests
from urllib.request import urlopen
from six import BytesIO #Used internally by PIL 
from PIL import Image, ImageDraw, ImageFont
import json


def printHello(): 
    url = "https://zillow56.p.rapidapi.com/property"

    querystring = {"zpid":"7594920"}

    headers = {
        "X-RapidAPI-Key": "2e7b06639bmshe0265e0dddf1f4fp17f3aajsn65bb8c0da710",
        "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)
    d=dict(response.json())
    path=d['hugePhotos'][0]['url']
    response = urlopen(path)
    image_data = response.read()
    image_data = BytesIO(image_data)
    image = Image.open(image_data)

    #return d["address"]["city"]
    return path


def read_city(): 
    
    d=json.load(open(r"app\data_file.json"))
    city=[]
    for house in d['results']:
        city.append(house['city'])
    return set(city)

def read_state(): 
    
    d=json.load(open(r"app\data_file.json"))
    state=[]
    for house in d['results']:
        state.append(house['state'])
    return set(state)

def read_with_prams(search_state, search_city): 
    
    d=json.load(open(r"app\data_file.json"))

    house_list=[]
    for house in d['results']:
        if house["state"]==search_state:
            if house["city"]==search_city:
                if house['homeStatus']== "FOR_SALE":
                    house_list.append(house)
    return house_list


def fetch():
    
    house_list=[{'bathrooms': 1.0,
    'bedrooms': 2.0,
    'city': 'Mesa',
    'country': 'USA',
    'currency': 'USD',
    'daysOnZillow': -1,
    'homeStatus': 'FOR_SALE',
    'homeStatusForHDP': 'FOR_SALE',
    'homeType': 'SINGLE_FAMILY',
    'isFeatured': False,
    'isNonOwnerOccupied': True,
    'isPreforeclosureAuction': False,
    'isPremierBuilder': False,
    'isUnmappable': False,
    'isZillowOwned': False,
    'latitude': 33.412533,
    'listing_sub_type': {'is_FSBA': True},
    'livingArea': 912.0,
    'longitude': -111.782074,
    'lotAreaUnit': 'sqft',
    'lotAreaValue': 6196.0,
    'price': 334900.0,
    'priceForHDP': 334900.0,
    'shouldHighlight': False,
    'state': 'AZ',
    'streetAddress': '2290 E Alpine Ave',
    'taxAssessedValue': 144000.0,
    'zipcode': '85204',
    'zpid': 7640489},
    {'bathrooms': 2.0,
    'bedrooms': 2.0,
    'city': 'Mesa',
    'country': 'USA',
    'currency': 'USD',
    'daysOnZillow': -1,
    'homeStatus': 'FOR_SALE',
    'homeStatusForHDP': 'FOR_SALE',
    'homeType': 'SINGLE_FAMILY',
    'isFeatured': False,
    'isNonOwnerOccupied': True,
    'isPreforeclosureAuction': False,
    'isPremierBuilder': False,
    'isUnmappable': False,
    'isZillowOwned': False,
    'latitude': 33.448643,
    'listing_sub_type': {'is_FSBA': True},
    'livingArea': 1335.0,
    'longitude': -111.67075,
    'lotAreaUnit': 'sqft',
    'lotAreaValue': 7579.44,
    'price': 397500.0,
    'priceForHDP': 397500.0,
    'shouldHighlight': False,
    'state': 'AZ',
    'streetAddress': '1843 N Avery Cir',
    'taxAssessedValue': 214600.0,
    'zipcode': '85207',
    'zpid': 8066821},
    {'bathrooms': 2.0,
    'bedrooms': 5.0,
    'city': 'Mesa',
    'country': 'USA',
    'currency': 'USD',
    'daysOnZillow': -1,
    'homeStatus': 'FOR_SALE',
    'homeStatusForHDP': 'FOR_SALE',
    'homeType': 'SINGLE_FAMILY',
    'isFeatured': False,
    'isNonOwnerOccupied': True,
    'isPreforeclosureAuction': False,
    'isPremierBuilder': False,
    'isUnmappable': False,
    'isZillowOwned': False,
    'latitude': 33.390846,
    'listing_sub_type': {'is_FSBA': True},
    'livingArea': 1860.0,
    'longitude': -111.8115,
    'lotAreaUnit': 'sqft',
    'lotAreaValue': 8407.08,
    'price': 396000.0,
    'priceForHDP': 396000.0,
    'shouldHighlight': False,
    'state': 'AZ',
    'streetAddress': '918 E Glade Ave',
    'taxAssessedValue': 215200.0,
    'zipcode': '85204',
    'zpid': 7629268},
    {'bathrooms': 2.0,
    'bedrooms': 4.0,
    'city': 'Mesa',
    'country': 'USA',
    'currency': 'USD',
    'datePriceChanged': 1678176000000,
    'daysOnZillow': -1,
    'homeStatus': 'FOR_SALE',
    'homeStatusForHDP': 'FOR_SALE',
    'homeType': 'SINGLE_FAMILY',
    'isFeatured': False,
    'isNonOwnerOccupied': True,
    'isPreforeclosureAuction': False,
    'isPremierBuilder': False,
    'isUnmappable': False,
    'isZillowOwned': False,
    'latitude': 33.465942,
    'listing_sub_type': {'is_FSBA': True},
    'livingArea': 2100.0,
    'longitude': -111.76836,
    'lotAreaUnit': 'sqft',
    'lotAreaValue': 9191.16,
    'price': 550000.0,
    'priceChange': -25000,
    'priceForHDP': 550000.0,
    'priceReduction': '$25,000 (Mar 7)',
    'shouldHighlight': False,
    'state': 'AZ',
    'streetAddress': '2906 E Nora St',
    'taxAssessedValue': 287200.0,
    'zipcode': '85213',
    'zpid': 7658739},
    {'bathrooms': 2.0,
    'bedrooms': 3.0,
    'city': 'Mesa',
    'country': 'USA',
    'currency': 'USD',
    'daysOnZillow': -1,
    'homeStatus': 'FOR_SALE',
    'homeStatusForHDP': 'FOR_SALE',
    'homeType': 'SINGLE_FAMILY',
    'isFeatured': False,
    'isNonOwnerOccupied': True,
    'isPreforeclosureAuction': False,
    'isPremierBuilder': False,
    'isUnmappable': False,
    'isZillowOwned': False,
    'latitude': 33.39715,
    'listing_sub_type': {'is_FSBA': True},
    'livingArea': 1266.0,
    'longitude': -111.82501,
    'lotAreaUnit': 'sqft',
    'lotAreaValue': 6155.0,
    'price': 384899.0,
    'priceForHDP': 384899.0,
    'shouldHighlight': False,
    'state': 'AZ',
    'streetAddress': '302 E 10th Ave',
    'taxAssessedValue': 159700.0,
    'zipcode': '85210',
    'zpid': 7632870},
    {'bathrooms': 3.0,
    'bedrooms': 3.0,
    'city': 'Mesa',
    'country': 'USA',
    'currency': 'USD',
    'daysOnZillow': -1,
    'homeStatus': 'FOR_SALE',
    'homeStatusForHDP': 'FOR_SALE',
    'homeType': 'SINGLE_FAMILY',
    'isFeatured': False,
    'isNonOwnerOccupied': True,
    'isPreforeclosureAuction': False,
    'isPremierBuilder': False,
    'isUnmappable': False,
    'isZillowOwned': False,
    'latitude': 33.422207,
    'listing_sub_type': {'is_FSBA': True},
    'livingArea': 1737.0,
    'longitude': -111.70896,
    'lotAreaUnit': 'sqft',
    'lotAreaValue': 3064.0,
    'price': 385000.0,
    'priceForHDP': 385000.0,
    'shouldHighlight': False,
    'state': 'AZ',
    'streetAddress': '5648 E Butte St',
    'taxAssessedValue': 238200.0,
    'zipcode': '85205',
    'zpid': 240311210},
    {'bathrooms': 2.0,
    'bedrooms': 4.0,
    'city': 'Mesa',
    'country': 'USA',
    'currency': 'USD',
    'daysOnZillow': -1,
    'homeStatus': 'FOR_SALE',
    'homeStatusForHDP': 'FOR_SALE',
    'homeType': 'SINGLE_FAMILY',
    'isFeatured': False,
    'isNonOwnerOccupied': True,
    'isPreforeclosureAuction': False,
    'isPremierBuilder': False,
    'isUnmappable': False,
    'isZillowOwned': False,
    'latitude': 33.38373,
    'listing_sub_type': {'is_FSBA': True},
    'livingArea': 1915.0,
    'longitude': -111.87146,
    'lotAreaUnit': 'sqft',
    'lotAreaValue': 7840.8,
    'price': 450000.0,
    'priceForHDP': 450000.0,
    'shouldHighlight': False,
    'state': 'AZ',
    'streetAddress': '1730 S Sycamore',
    'taxAssessedValue': 246000.0,
    'zipcode': '85202',
    'zpid': 7600516}]
    
    return house_list
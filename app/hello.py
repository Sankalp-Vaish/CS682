import requests
from urllib.request import urlopen
from six import BytesIO #Used internally by PIL 
from PIL import Image, ImageDraw, ImageFont


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
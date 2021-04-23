import matplotlib.pyplot as plt
import requests
from PIL import Image
import urllib.request
import json
import re
class GoogleMapsConnection:
    def __init__(self):

        self.api_file = open(r'C:\Users\emils\Desktop\API_Key.txt')
        self.api_key = self.api_file.read()
        self.api_file.close()
        self.lat = 0.0
        self.lng = 0.0

    #Henter en Json fil for byen du giver i en string
    def get_city_json(self,city):
        try:
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + city + '&key=' + self.api_key
            resp = requests.get(url)
            data = resp.json()
            test = json.dumps([s['geometry']['location'] for s in data['results']])
            dict = json.loads(test[1:-1])
            self.lat = dict.get('lat')
            self.lng = dict.get('lng')
        except:
            print("Something got fucked when getting city json")


    def getIMG(self):
        try:
            print(self.lat)
            print(self.lng)

            r = requests.get('https://maps.googleapis.com/maps/api/staticmap?center=' + str(self.lat) + ',' + str(self.lng) + '&zoom=12&size=600x600&key=' + self.api_key)

            file = open("sample_image.png", "wb")
            file.write(r.content)
            file.close()

            image = Image.open('sample_image.png')
            return image
        except:
            print('could not fetch image :/')
            print(r)




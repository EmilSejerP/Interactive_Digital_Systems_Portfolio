import matplotlib.pyplot as plt
import requests
from PIL import Image
import urllib.request
import json
import re
import os

class GoogleMapsConnection:
    def __init__(self):
        path = os.path.expanduser("~/Desktop") + ('\API_Key.txt')

        try:
            self.api_file = open(path) #open google api key
        except:
            print("Could not fetch API key, is it missing?")

        print(path)

        print(self.api_file)
        self.api_key = self.api_file.read()                         #read the api key file
        self.api_file.close()                                       #close
        self.lat = 0.0                                              #inits 
        self.lng = 0.0

    #Henter en Json fil for byen du giver i en string
    def get_city_json(self,city):
        try:
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + city + '&key=' + self.api_key #fetch url with api-key
            resp = requests.get(url)                                                                           #fetch the data from the address
            data = resp.json()                                                                                 #read as json 
            test = json.dumps([s['geometry']['location'] for s in data['results']])                            #save geometry and location data for all results
            dict = json.loads(test[1:-1])                                                                      #load as dictionary again
            self.lat = dict.get('lat')                                                                         #latitude in dict        
            self.lng = dict.get('lng')                                                                         #longitude in dict
        except:
            print("Something went wrong when fetching json file for city. Check your API key.")


    def getIMG(self):
        try:
            #print(self.lat) 
            #print(self.lng)

            r = requests.get('https://maps.googleapis.com/maps/api/staticmap?center=' + str(self.lat)
                           + ',' + str(self.lng)
                           + '&zoom=12&size=600x600&key=' 
                           + self.api_key) #fetch the image data from gmaps with the longitude and latitude provided earlier

            file = open("sample_image.png", "wb") #open arbitrary init image
            file.write(r.content)                 #write the image data from gmaps to that image
            file.close()                          #

            image = Image.open('sample_image.png') #then read the file as an image
            return image
        except:
            print('Could not fetch image :/, make sure your API key is correct.')





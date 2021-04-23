from Graph import *
from UserInput import *
from KMeansAlgorithm import *
from GoogleMapsConnection import *
def main():

    graph = Graph()               #Init graph          
    gapi = GoogleMapsConnection() #Init google maps api

    gapi.get_city_json('Roskilde') #Fetch the coordinates 
    img = gapi.getIMG()            #Fetch picture 

    kmeans = KMeansAlgorithm(2)      #Init KMeans algoritmen
    usein = UserInput(graph,kmeans) #Init UserInput klassen

    graph.set_background(img) #Sætter graph baggrunden til img variablen
    graph.updateGraph()       #Opdatere og viser grafen


if __name__ == "__main__":
    main()
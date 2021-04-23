from Graph import *
from UserInput import *
from KMeansAlgorithm import *
from GoogleMapsConnection import *
def main():

    #Init graph
    graph = Graph()
    #Init google maps api
    gapi = GoogleMapsConnection()

    #Fetch the picture from google maps api
    gapi.get_city_json('Roskilde')
    img = gapi.getIMG()

    #Init KMeans algoritmen
    kmeans = KMeansAlgorithm()
    #Init UserInput klassen
    usein = UserInput(graph,kmeans)

    #Sætter graph baggrunden til img variablen
    graph.set_background(img)

    #Opdatere og viser grafen
    graph.updateGraph()

if __name__ == "__main__":
    main()
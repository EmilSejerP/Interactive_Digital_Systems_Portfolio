from Graph import *
from UserInput import *
from KMeansAlgorithm import *
from GoogleMapsConnection import *
from App import *

def main():
    app = App()
    app.run()
    centroidAmnt = int(App.clusterAmount)
    graph = Graph(centroidAmnt)               #Init graph          
    gapi = GoogleMapsConnection() #Init google maps api
    gapi.get_coord_json(App.loc) #Fetch the coordinates
    img = gapi.get_image()            #Fetch picture
    graph.set_background(img)  # Sætter graph baggrunden til img variablen

    kmeans = KMeansAlgorithm(centroidAmnt)  #Init KMeans algoritmen
    usein = UserInput(graph,kmeans)         #Init UserInput klassen

    graph.update_graph()       #Opdatere og viser grafen


if __name__ == "__main__":
    main()
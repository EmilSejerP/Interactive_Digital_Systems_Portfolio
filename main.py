from Graph import *
from UserInput import *
from KMeansAlgorithm import *
from GoogleMapsConnection import *
from dotenv import dotenv_values

#load_dotenv()  # take environment variables from .env.

#config = {
#    **dotenv_values(".env.shared"),  # load shared development variables
#    **dotenv_values(".env.secret"),  # load sensitive variables
#    **os.environ,  # override loaded values with environment variables
#}

def main():
    kmeans = KMeansAlgorithm(4)     #Init KMeans algoritmen
    graph = Graph(kmeans.n)         #Init graph          
    usein = UserInput(graph,kmeans) #Init UserInput klassen

    gapi = GoogleMapsConnection()  #Init google maps api
    gapi.get_city_json('Roskilde') #Fetch the coordinates 
    img = gapi.getIMG()            #Fetch picture 

    

    graph.set_background(img) #Sætter graph baggrunden til img variablen
    graph.updateGraph()       #Opdatere og viser grafen


if __name__ == "__main__":
    main()
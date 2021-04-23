import matplotlib.pyplot as plt
import numpy as np
import math
import urllib.request
import PIL
import random as rand
class Graph:

    # Init creates empty graph
    def __init__(self):                     #graph constructor
        self.fig, self.ax = plt.subplots()  #init graph components
        self.centroidToPoints = {}          #points connected to centroids
        self.lst_cluster_a = []             #cluster from 1 centroid
        self.lst_cluster_b = []
        self.edgesArray = {}                #All edges passing from a given point

    #Create TSP
    def calculate_edges(self, lst): #calculate the distance from a given point to all other points in the array.
        for i in range(len(lst)):
            for j in range(len(lst)):
                edge_dist = math.sqrt(((lst[i][1][0]-lst[j][1][0])**2) + ((lst[i][1][1]-lst[j][1][1])**2))
                #if(lst[i][0] == 1)

    # Creates a connection to the graph which allows us to check for mouse clicks.
    def connect_to_graph(self, typeEvent, typeUserInput):   
        self.fig.canvas.mpl_connect(typeEvent, typeUserInput)

    # Creates a new plot taking event data on graph
    def draw_new_store(self, event):
            self.ax.plot(event.xdata, event.ydata, 'o')

    # Creates centroids

    #def draw_new_centroid(self,centroid):
    #    self.ax.plot(centroid[0], centroid[1], 'X')

    #takes an array of centroids and plots them on the graph
    def draw_new_centroids(self, centroids):
        for centroid in centroids:
            self.ax.plot(centroid[0], centroid[1], 'X')

    #def draw_new_centroids(self, centroid1, centroid2):
    #    self.ax.plot(centroid1[0], centroid1[1], 'X')
    #    self.ax.plot(centroid2[0], centroid2[1], 'X')
    
    def remove_old(self,n):
        if len(self.ax.lines) > 5:
            for i in range(n):
                self.ax.lines.pop()

    def rgb_to_hex(self,rgb):
        return '#'+'%02x%02x%02x' % rgb

    def recolor(self,lst,n,amntVertices):
        color_dict = {}

        for j in range(n):                                  #Generate colors
            color = self.rgb_to_hex((rand.randint(0, 255),rand.randint(0, 255),rand.randint(0, 255)))
            color_dict.update({j:color})

        print(color_dict)

        for i in range(len(self.ax.lines)):
            
            for key in color_dict:
                print(key)
                print(i)

                if lst[i][0] == key:
                    self.ax.lines[i].set_color(color_dict[key])


        print(self.lst_cluster_a)


    def set_background(self,img):
        self.ax.imshow(img)

    # Updates graph
    def updateGraph(self):
        plt.show()

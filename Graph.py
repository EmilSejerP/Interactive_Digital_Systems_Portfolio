import matplotlib.pyplot as plt
import numpy as np
import math
import urllib.request
import PIL
import random as rand

class Graph:
    # Init creates empty graph
    def __init__(self, n):                     #graph constructor
        self.fig, self.ax = plt.subplots()  #init graph components
        self.centroidToPoints = {}          #points connected to centroids
        self.lst_cluster_a = []             #cluster from 1 centroid
        self.lst_cluster_b = []
        self.edgesArray = {}                #All edges passing from a given point
        self.n = n
        self.color_dict = {}

        for j in range(n): #Generate colors                             
            color = self.rgb_to_hex((rand.randint(0, 255),rand.randint(0, 255),rand.randint(0, 255)))
            self.color_dict.update({j:color})

    # Creates a connection to the graph which allows us to check for mouse clicks.
    def connect_to_graph(self, typeEvent, typeUserInput):   
        self.fig.canvas.mpl_connect(typeEvent, typeUserInput)

    # Creates a new plot taking event data on graph
    def draw_new_store(self, event):
            self.ax.plot(event.xdata, event.ydata, 'o')

    #takes an array of centroids and plots them on the graph
    def draw_new_centroids(self, centroids):
        for centroid in centroids:
            self.ax.plot(centroid[0], centroid[1], 'X')

    #removes old centroids from the graph plot.
    def remove_old(self,n):
        if len(self.ax.lines) > 5:
            for i in range(n):
                self.ax.lines.pop()
                print("popped")

    def rgb_to_hex(self,rgb):
        return '#'+'%02x%02x%02x' % rgb

    def divideCentroids(self):
        for i in range(amntVertices):   
            if lst[i][0] == key:
                centroidToPoints.update()

    #recolors stores according to centroids/cluster
    def recolor(self,lst,amntVertices):
        for i in range(amntVertices):   
            for key in self.color_dict:
                if lst[i][0] == key:
                    self.ax.lines[i].set_color(self.color_dict[key])

    def set_background(self,img):
        self.ax.imshow(img)

    # Updates graph
    def updateGraph(self):
        plt.show()

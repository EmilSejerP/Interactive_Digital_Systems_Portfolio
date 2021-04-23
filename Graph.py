import matplotlib.pyplot as plt
import numpy as np
import math
import urllib.request
import PIL

class Graph:

    # Init creates empty graph
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.lst_cluster_a = []
        self.lst_cluster_b = []
        self.edgesArray = {}

    #Create TSP
    def calculate_edges(self, lst):
        for i in range(len(lst)):
            for j in range(len(lst)):
                edge_dist = math.sqrt(((lst[i][1][0]-lst[j][1][0])**2) + ((lst[i][1][1]-lst[j][1][1])**2))
                #if(lst[i][0] == 1)

    # Creates a connection to the graph
    def connect_to_graph(self, typeEvent, typeUserInput):
        self.fig.canvas.mpl_connect(typeEvent, typeUserInput)

    # Creates a new plot taking event data on graph
    def draw_new_store(self, event):
            self.ax.plot(event.xdata, event.ydata, 'o')

    # Creates centroids
    def draw_new_centroids(self, centroid1, centroid2):
        self.ax.plot(centroid1[0], centroid1[1], 'X')
        self.ax.plot(centroid2[0], centroid2[1], 'X')
    
    def remove_old(self):
        if len(self.ax.lines) > 5:
            self.ax.lines.pop()
            self.ax.lines.pop()

    def recolor(self,lst):
        self.lst_cluster_a = []
        self.lst_cluster_b = []
        for i in range(len(self.ax.lines)):
            if lst[i][0] == 1:
                self.ax.lines[i].set_color('red')
                self.lst_cluster_a.append([self.ax.lines[i].get_xdata()[0],self.ax.lines[i].get_ydata()[0]])
            else:
                self.ax.lines[i].set_color('green')   
                self.lst_cluster_b.append([self.ax.lines[i].get_xdata()[0],self.ax.lines[i].get_ydata()[0]])
        print(self.lst_cluster_a)

    def set_background(self,img):
        self.ax.imshow(img)

    # Updates graph
    def updateGraph(self):
        plt.show()

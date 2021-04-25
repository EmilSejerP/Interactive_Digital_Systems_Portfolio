import matplotlib.pyplot as plt
import math
import random as rand

class Graph:
    # Init creates empty graph
    def __init__(self, n):                     #graph constructor
        self.fig, self.ax = plt.subplots()  #init graph components
        self.n = n
        self.color_dict = {}

        for j in range(n): #Generate colors                             
            color = self.rgb_to_hex((rand.randint(0, 255),rand.randint(0, 255),rand.randint(0, 255)))
            self.color_dict.update({j:color})

    def connect_to_graph(self, type_event, type_user_input):
        self.fig.canvas.mpl_connect(type_event, type_user_input)       #Creates connection to graph

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
        self.ax.plot(event.xdata, event.ydata, 'o')             #Creates a 'o' marker at xdata, ydata location

    def draw_new_centroids(self, centroids):
        for centroid in centroids:
            self.ax.plot(centroid[0], centroid[1], 'X')             #Creates 'X' marker for every centroid passed
    
    def remove_old(self,n):                                         #Bedre kommentar her :)
        if len(self.ax.lines) > 5:
            for i in range(n):
                self.ax.lines.pop()                                 #Pops from ax.lines equal to amount of clusters

    def rgb_to_hex(self,rgb):                                       #Method to hexify input
        return '#'+'%02x%02x%02x' % rgb

    def divideCentroids(self):
        for i in range(amntVertices):   
            if lst[i][0] == key:
                centroidToPoints.update()

    #recolors stores according to centroids/cluster
    def recolor(self,lst,n):
        print(len(lst))
        print(len(self.ax.lines))

        for i in range(len(self.ax.lines)):
            for key in self.color_dict:
                if lst[i][0] == key:
                    self.ax.lines[i].set_color(self.color_dict[key])
   
            
    def set_background(self,img):
        self.ax.imshow(img)                                         #Sets the background to img

    # Updates graph
    def update_graph(self):                                         #updates graph
        plt.show()

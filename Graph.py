import matplotlib.pyplot as plt
import math
import random as rand

class Graph:

    def __init__(self):                     #graph constructor
        self.fig, self.ax = plt.subplots()  #init graph components


    def connect_to_graph(self, type_event, type_user_input):
        self.fig.canvas.mpl_connect(type_event, type_user_input)       #Creates connection to graph

    def draw_new_store(self, event):
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

    def recolor(self,lst,n):                                        #Recolors 'o' markers
        color_dict = {}                                             #Creates dict for colors index equals to cluster labels
        for j in range(n):
            color = self.rgb_to_hex((rand.randint(0, 255),rand.randint(0, 255),rand.randint(0, 255)))
            color_dict.update({j:color})

        for i in range(len(lst)):                                   #Where dict index and cluster lable are the same
            for key in color_dict:
                if lst[i][0] == key:
                    self.ax.lines[i].set_color(color_dict[key])     #Set the color of ax.lines

    def set_background(self,img):
        self.ax.imshow(img)                                         #Sets the background to img

    # Updates graph
    def update_graph(self):                                         #updates graph
        plt.show()

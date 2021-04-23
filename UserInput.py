class UserInput:

    # initiation that takes graph argument and attaches this UserInput class to that specific graph
    def __init__(self,graph,KMeans):
        self.graph = graph
        self.KMeans = KMeans
        #Connects to graph
        graph.connect_to_graph('button_press_event', self.onMouseClick)


    #Takes mouse click input and class to draw on graph and update the graph
    def onMouseClick(self,event):
        self.graph.remove_old()
        self.KMeans.updateStoreArray([event.xdata, event.ydata])
        self.graph.draw_new_store(event)
        if self.KMeans.calculateKMeans() != 0:
            self.graph.recolor(self.KMeans.getZipped(),2)
            self.graph.calculate_edges(self.KMeans.getZipped())
            calc = self.KMeans.calculateKMeans()
            self.graph.draw_new_centroids(calc)
        else:
            print("not ready for centroids")
        self.graph.updateGraph()


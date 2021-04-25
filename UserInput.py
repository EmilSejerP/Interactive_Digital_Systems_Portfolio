class UserInput:

    # initiation that takes graph argument and attaches this UserInput class to that specific graph
    def __init__(self,graph,KMeans):
        self.graph = graph
        self.KMeans = KMeans
        self.graph.connect_to_graph('button_press_event', self.on_mouse_click)


    #Takes mouse click input and class to draw on graph and update the graph
    def on_mouse_click(self, event):
        self.graph.remove_old(self.KMeans.n)
        self.KMeans.update_store_list([event.xdata, event.ydata])
        self.graph.draw_new_store(event)
        if self.KMeans.calculate_kmeans() != 0:
            calc = self.KMeans.calculate_kmeans()
            self.graph.draw_new_centroids(calc)
            self.graph.recolor(self.KMeans.get_zipped(), self.KMeans.n)
        else:
            print("not ready for centroids")
        self.graph.update_graph()


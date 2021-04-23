from sklearn.cluster import KMeans as K


class KMeansAlgorithm:
    def __init__(self, amountOfClusters):
        self.n = amountOfClusters
        self.arrayOfStores = []
        self.zipped = []

    # Call to update array for kmeans
    def updateStoreArray(self, coords):
        self.arrayOfStores.append(coords)

    # Calculates KMeans if there is more than 4 stores in the array
    def calculateKMeans(self):
        if len(self.arrayOfStores) > 4:                                  #if number of stores are above 4 calculate kmeans.
            kmeans = K(n_clusters=self.n)                                #init amount of clusters to input n value.   
            kmeans.fit(self.arrayOfStores)                               #fit the kmeans to the store array.   
            self.zipped = list(zip(kmeans.labels_, self.arrayOfStores))  #create a list of the stores and the kmeans label, which can be used to identify which stores are in which clusters
            clusters = kmeans.cluster_centers_                           #save the kmeans clusters.

            for i in range(self.n):                                      #for all the kmeans clusters
                cluster1 = [clusters[i][i], clusters[i][i+1]]            #create the cluster from data
                returnClusters.append(cluster1)                          #append them to the return array.

            return returnClusters                                        #Return the clusters.
        else:
            print("Need more stores to calculate KMeans")
            return 0

    def getZipped(self):
        return self.zipped

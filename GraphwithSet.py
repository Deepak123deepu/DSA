import abc 
import numpy as np 

class Graph(abc.ABC):

    def __init__(self,numberOfVertices, directed = False):
        self.numberOfVertices = numberOfVertices
        self.directed = directed 

    @abc.abstractmethod
    def add_node(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacenct_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self,v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self,v1,v2):
        pass 

    @abc.abstractmethod
    def display(self):
        pass 



class node:

    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacencySet = set()

    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError("Vertex cannot be adjancent to itself")
        
        self.adjacencySet.add(v)

    def get_adjacenct_vertices(self):
        return sorted(self.adjacencySet)




class AdjacencySetGraph(Graph):
    def __init__(self, numberOfVertices, directed = False): 
        super().__init__(numberOfVertices, directed) 
        
        self.vertix_list = []
        for i in range(numberOfVertices):
            self.vertix_list.append(node(i)) 

    def add_node(self, v1, v2, weight=1):
    
        if v1 >= self.numberOfVertices or v2 >= self.numberOfVertices or v1 < 0 or v2 < 0:
            return ValueError("vertex are out of range ra swami")

        if weight != 1: # represent only unweighted graphs (edge weight cannot be greater than 1)
            return ValueError("edge can't be < 1") 
        
        self.vertix_list[v1].add_edge(v2)

        if self.directed == False:
            self.vertix_list[v2].add_edge(v1)


    def get_adjacenct_vertices(self, v):
    
        if v < 0 and v >= self.numberOfVertices:
            raise ValueError("can't access vertices " + str(v))

        return self.vertix_list[v].get_adjacenct_vertices()

    def get_indegree(self,v):
        if v < 0 and v >= self.numberOfVertices:
            raise ValueError("can't access vertices " + str(v))

        Indegree = 0 

        for i in range(self.numberOfVertices):
            if v in self.get_adjacenct_vertices(i):
                Indegree += 1
        return Indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.numberOfVertices):
            for v in self.get_adjacenct_vertices(i):
                print(i, "-->", v)


grp = AdjacencySetGraph(4)

grp.add_node(0,1)
grp.add_node(0,2)
grp.add_node(2,3)

for i in range(4):
    print("adjacenct to ", i , grp.get_adjacenct_vertices(i))

for i in range(4):
    print("adjacenct to ", i , grp.get_indegree(i))

for i in range(4):
    for j in grp.get_adjacenct_vertices(i):
        print("edge weight", i, " ",j , "weight:", grp.get_edge_weight(i,j))


grp.display()

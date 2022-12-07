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


class AdjacencyMatricx(Graph):

    def __init__(self, numberOfVertices, directed = False): 

        super().__init__(numberOfVertices, directed) 
        self.matrix = np.zeros((numberOfVertices,numberOfVertices))

    def add_node(self, v1, v2, weight=1):

        if v1 >= self.numberOfVertices or v2 >= self.numberOfVertices or v1 < 0 or v2 < 0:
            return ValueError("vertex are out of range ra swami")

        if weight < 1:
            return ValueError("edge can't be < 1") 

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight 

    def get_adjacenct_vertices(self, v):

        if v < 0 and v >= self.numberOfVertices:
            raise ValueError("can't access vertices " + str(v))

        Adjacency_vertices = []

        for i in range(self.numberOfVertices):
            if self.matrix[v][i] >0 :
                Adjacency_vertices.append(i)

        return Adjacency_vertices 

    def get_indegree(self,v):
        if v < 0 and v >= self.numberOfVertices:
            raise ValueError("can't access vertices " + str(v))

        indegree = 0 
        for i in range(self.numberOfVertices):
            if self.matrix[i][v] > 0 :
                indegree += 1 
        
        return indegree 

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numberOfVertices):
            for v in self.get_adjacenct_vertices(i):
                print(i, "-->", v)

        
grp = AdjacencyMatricx(4)

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
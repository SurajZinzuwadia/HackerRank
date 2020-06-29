class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list = {}
        for node in range(self.nodes):
            self.adj_list[node] = []

        self.tc = [[0 for j in range(self.nodes)] for i in range(self.nodes)]
    def add_edge(self,u,v):
        self.adj_list[u].append(v)

    def print_adj_list(self):
        for node in range(self.nodes):
            print(node, "->" , self.adj_list[node])

    def DFSUtil(self,s,v):
        self.tc[s][v] = 1
        for i in self.adj_list[v]:
            if self.tc[s][i] == 0:
                self.DFSUtil(s,i)

    def transitiveClosure(self):
        for i in range(self.nodes):
            self.DFSUtil(i,i)
        print(self.tc)


if __name__ == "__main__":
    V  = 5
    graph = Graph(V)
    all_edges = [ (0,1) ,(0,4) ,(1,2) ,(1,3) ,(1,4) ,(2,3) ,(3,4) ]
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.print_adj_list()
    graph.transitiveClosure()
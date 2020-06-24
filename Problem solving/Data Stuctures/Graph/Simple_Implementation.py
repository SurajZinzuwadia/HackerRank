from queue import Queue
class Graph:
    def __init__(self,Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        if not self.is_directed:
            self.adj_list[v].append(u)

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->" , self.adj_list[node])




if __name__ == "__main__":
    V  = [0,1,2,3,4]
    graph = Graph(V)
    all_edges = [ (0,1) ,(0,4) ,(1,2) ,(1,3) ,(1,4) ,(2,3) ,(3,4) ]
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.print_adj_list()

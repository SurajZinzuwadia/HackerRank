class Graph:
    def __init__(self,Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self,u,v,w):
        self.adj_list[u].append([v,w])
        if not self.is_directed:
            self.adj_list[v].append([u,w])

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->" , self.adj_list[node])

    def longestPath(self,s):
        dist = [-1] * len(self.adj_list)
        dist[s] = 0

        for _ in range(len(self.nodes)-1):
            for v,w in self.adj_list[_]:
                if(dist[_]!= -1 and dist[_] + w > dist[v]):
                    print(dist)
                    dist[v] = dist[_] + w
        print(dist)
if __name__ == "__main__":
    V  = [0,1,2,3,4,5,6]
    graph = Graph(V)
    all_edges = [ (1,2,3) ,(2,3,4) ,(2, 6,2) ,(6, 4,6)  ,(6,5,5)]
    for u,v,w in all_edges:
        graph.add_edge(u,v,w)
    graph.print_adj_list()
    graph.longestPath(1)

from queue import Queue
class Graph:
    def __init__(self,Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self,u,v,w):
        self.adj_list[u].append([v,w])
        # if not self.is_directed:
        #     self.adj_list.append([v,u,w])

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->" , self.adj_list[node])

    def BellmanFord(self,s):
        dist = [float("Inf")] * len(self.adj_list)
        dist[s] = 0

        for _ in range(len(self.nodes)-1):
            for v,w in self.adj_list[_]:
                if(dist[_]!= float("Inf") and dist[_] + w < dist[v]):
                    print(dist)
                    dist[v] = dist[_] + w
        print(dist)


if __name__ == "__main__":
    V  = [0,1,2,3,4,5]
    graph = Graph(V)
    all_edges = [ (0, 1, -1)  ,(0, 2, 4)  , (1, 2, 3) , (1, 3, 2) , (1, 4, 2)  , (3, 2, 5)  , (3, 1, 1)  , (4, 3, -3)   ]
    for u,v,w in all_edges:
        graph.add_edge(u,v,w)
    graph.print_adj_list()
    graph.BellmanFord(0)

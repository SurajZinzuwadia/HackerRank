
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

    def BellmanFord(self,s):
        dist = [float("Inf")] * len(self.adj_list)
        dist[s] = 0

        for _ in range(len(self.nodes)-1):
            for v,w in self.adj_list[_]:
                if( dist[_] + w < dist[v]):
                    # print(dist)
                    dist[v] = dist[_] + w
        return dist


if __name__ == "__main__":
    v,N = input().split()
    v = int(v)
    N = int(N)
    V = []
    for i in range(0,(v)):
        V.append(i)
    graph = Graph(V)
    all_edges = []
    for i in range(0,N):
        all_edges.append(map(int,(input().strip().split())))
    for u,v,w in all_edges:
        graph.add_edge(u-1,v-1,2**w)
    # graph.print_adj_list()
    for i in range(0,v):
        dist = graph.BellmanFord(v)
    dist_sum = sum(dist) + 1
    print(bin(dist_sum)[2:])
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
        # if not self.is_directed:
        #     self.adj_list[v].append(u)

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->" , self.adj_list[node])

    def DFSUtil(self,v,visited):
        visited[v] = True
        for i in self.adj_list[v]:
            if visited[i] == False:
                self.DFSUtil(i,visited)

    def mother_vertex(self):
        visited = {}
        for node in self.adj_list.keys():
            visited[node] = False
        s = 0

        for i in range(len(self.nodes)):
            if (visited[i] == False):
                self.DFSUtil(i,visited)
                s=i
        print(s)
        for node in self.adj_list.keys():
            visited[node] = False
        self.DFSUtil(s,visited)
        print(visited)
        if any(i == False for i in visited.values()):
            print(-1)
        else:
            print(s)




if __name__ == "__main__":
    V  = [0,1,2,3,4,5,6]
    graph = Graph(V)
    all_edges = [ (0, 1) ,(0,2) ,(1,3) , (4,1) , (6,4) , (5,6), (5,2) , (6,0)]
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.print_adj_list()
    graph.mother_vertex()


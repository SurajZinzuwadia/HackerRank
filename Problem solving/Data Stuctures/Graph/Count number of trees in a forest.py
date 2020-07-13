
class Graph:
    def __init__(self,Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self,u,v):
        self.adj_list[u].append(v)

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->" , self.adj_list[node])

    def DFSUtil(self,u,visited):
        visited[u] = True
        for i in self.adj_list[u]:
            if visited[i] == False:
                self.DFSUtil(i,visited)


    def countTrees(self):
        visited = [False] * len(self.nodes)
        result = 0
        for i in self.nodes:
            if (visited[i] == False):
                result+=1
                self.DFSUtil(i,visited)

        print(result)

if __name__ == "__main__":
    V  = [0,1,2,3,4]
    graph = Graph(V)
    all_edges = [ (0,1) ,(1,2) , (3,4)]
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.print_adj_list()
    graph.countTrees()
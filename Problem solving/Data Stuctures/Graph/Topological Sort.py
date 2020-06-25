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

    def topologicalUtil(self,u,visited,stack):
        visited[u] = True
        for i in self.adj_list[u]:
            if visited[i] == False:
                self.topologicalUtil(i,visited,stack)
        stack.insert(0,u)

    def topologicalSort(self):
        visited = [False] * len(self.nodes)
        print(visited)
        stack = []
        for u in self.nodes:
            if visited[u]== False:
                self.topologicalUtil(u,visited,stack)

        print(stack)
if __name__ == "__main__":
    V  = [0,1,2,3,4,5]
    graph = Graph(V)
    all_edges = [ (5,2) ,(5,0) ,(4, 0) ,(4, 1)  ,(3,1) ,(2,3)]
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.topologicalSort()

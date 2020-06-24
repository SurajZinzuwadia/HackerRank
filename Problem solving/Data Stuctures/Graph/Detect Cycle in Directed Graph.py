class Graph:
    def __init__(self,Nodes, is_directed = True):
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


    def isCyclicUtil(self,v,visited , restack):
        visited[v] = True
        restack[v] = True
        for i in self.adj_list[v]:
            if (v ==2):
                print("i",i)
            if visited[i] == False:
                if self.isCyclicUtil(i,visited,restack) == True:
                    return True
            elif( restack[i] == True):
                return True
        restack[v] = False
        print(v,restack[v])
        return False

    def Cyclic(self):
        visited = {}
        restack = [False] * len(self.adj_list)
        for node in self.adj_list.keys():
            visited[node] = False
        for node in self.adj_list:
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, restack) == True:
                    return True
        print(restack,visited)
        return False


if __name__ == "__main__":
    V  = [0,1,2,3]
    graph = Graph(V)
    all_edges = [ (0,1) ,(0,2) ,(1,2) ]
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.print_adj_list()
    if graph.Cyclic() == True:
        print("Contain cycle")
    else:
        print("Not Contain cycle")
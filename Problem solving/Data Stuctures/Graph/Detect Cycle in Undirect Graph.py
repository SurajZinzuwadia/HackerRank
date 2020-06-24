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


    def isCyclicUtil(self,v,visited ,parent):
        visited[v] = True
        print("v->",v)
        for i in self.adj_list[v]:
            print("parent->i",parent,i)
            if visited[i] == False:
                if self.isCyclicUtil(i,visited,v):
                    return True
            elif( parent >i):
                print(v,parent,i)
                return True
        return False


    def Cyclic(self):
        visited = {}
        for node in self.adj_list.keys():
            visited[node] = False
        for node in self.adj_list:
            if visited[node] == False:
                if (self.isCyclicUtil(node, visited, -1) )== True:
                    return True
        return False


if __name__ == "__main__":
    V  = [0,1,2,3,4]
    graph = Graph(V)
    all_edges = [ (0,1) , (1,2) , (2,3) ,(3,4) ,(4,1)]
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.print_adj_list()
    if graph.Cyclic():
        print("Contain cycle")
    else:
        print("Not Contain cycle")
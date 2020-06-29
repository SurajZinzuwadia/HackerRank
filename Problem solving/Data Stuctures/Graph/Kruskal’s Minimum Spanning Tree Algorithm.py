
class Graph:
    def __init__(self,Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = []
        self.is_directed = is_directed

    def add_edge(self,u,v,w):
        self.adj_list.append([u,v,w])
        # if not self.is_directed:
        #     self.adj_list.append([v,u,w])

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->" , self.adj_list[node])

    def find_parents(self,parents,i):
        if parents[i] == -1:
            return i
        elif parents[i] !=-1:
            return self.find_parents(parents,parents[i])

    def union(self,parents,u,v):
        x_set = self.find_parents(parents,u)
        y_set = self.find_parents(parents,v)
        parents[x_set] = y_set

    def krushkal(self):
        e = 0
        i = 0
        self.adj_list = sorted(self.adj_list, key=lambda item: item[2])
        print(self.adj_list)
        result = []
        parents = [-1] * len(self.nodes)
        while e < len(self.nodes)-1:
            u,v,w = self.adj_list[i]
            i=i+1
            x = self.find_parents(parents,u)
            y = self.find_parents(parents,v)
            if (x!=y):
                e = e + 1
                result.append([u,v,w])
                self.union(parents,x,y)
            print(parents)
        for u,v,weight  in result:
            print ("%d -- %d == %d" % (u,v,weight))


if __name__ == "__main__":
    V  = [0,1,2,3]
    graph = Graph(V)
    all_edges = [ (0, 1, 10)  ,(0, 2, 6)  , (0,3,5)  , (1,3,15) , (2,3,4)  ]
    for u,v,w in all_edges:
        graph.add_edge(u,v,w)
    # graph.print_adj_list()
    graph.krushkal()

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

    def is_reachable(self,u,v):
            queue = Queue()
            queue.put(u)
            visited = {}
            for node in self.adj_list.keys():
                visited[node] = False
            flag = 0
            visited[u] = True
            while not queue.empty():
                print(list(queue.queue))
                u = queue.get()
                if (self.adj_list[u].__contains__(v)):
                    flag = 1
                    break
                else:
                    for x in self.adj_list[u]:
                        if (visited[x] == False):
                            queue.put(x)
                        else:
                            break
            if( flag == 1):
                print("the path is ", u, "to", v)
                print("yes")
            else:
                print("Not Reachable")
if __name__ == "__main__":
    V  = [0,1,2,3]
    graph = Graph(V)
    all_edges = [ (0, 1) ,(0,2) ,(1,2) , (2,0),(2,3) ]
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.print_adj_list()
    graph.is_reachable(1,3)

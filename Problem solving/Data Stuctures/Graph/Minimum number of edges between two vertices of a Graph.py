from queue import Queue
class Graph:
    def __init__(self,Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []

    def addEdge(self,u,v):
        self.adj_list[u].append(v)

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->" , self.adj_list[node])

    def minEdgeBFS(self,s,d):
        visited = [False] * len(self.nodes)
        distance = [0] * len(self.nodes)
        q =   Queue()
        q.put(s)
        distance[s] = 0
        visited[s] = True
        while (not q.empty()):
            x = q.get()
            for i in self.adj_list[x]:
                if(visited[i] == True):
                    continue
                distance[i] = distance[x] + 1
                q.put(i)
                visited[i] = True
        print(distance[d])
if __name__ == "__main__":
    V  = [0,1,2,3,4,5,6,7,8,9]
    graph = Graph(V)
    graph.addEdge( 0, 1)
    graph.addEdge( 0, 7)
    graph.addEdge( 1, 7)
    graph.addEdge( 1, 2)
    graph.addEdge( 2, 3)
    graph.addEdge( 2, 5)
    graph.addEdge( 2, 8)
    graph.addEdge( 3, 4)
    graph.addEdge( 3, 5)
    graph.addEdge( 4, 5)
    graph.addEdge( 5, 6)
    graph.addEdge( 6, 7)
    graph.addEdge( 7, 8)
    graph.print_adj_list()
    graph.minEdgeBFS(0,5)

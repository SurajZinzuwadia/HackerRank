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



    def BFS(self):
        print(self.adj_list)
        visited = {}
        level = {}
        parent = {}
        bfs_traversal_output = []
        queue = Queue()
        for node in self.adj_list.keys():
            visited[node] = False
            parent[node] = None
            level[node] = -1
        s = 2
        visited[s] = True
        level[s] = 0
        queue.put(s)
        while not queue.empty():
            u = queue.get()
            bfs_traversal_output.append(u)
            for v in self.adj_list[u]:
                if  not visited[v]:
                    visited[v] = True
                    level[v] = level[u] + 1
                    queue.put(v)
        print(bfs_traversal_output)


if __name__ == "__main__":
    V  = [0,1,2,3,4]
    graph = Graph(V)
    all_edges = [ (0,1) ,(0,2) ,(1,2) ,(2,0) ,(2,3) ]
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.BFS()
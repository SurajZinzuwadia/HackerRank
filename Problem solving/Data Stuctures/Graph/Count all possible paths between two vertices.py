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

    def countPaths(self, s, d):

        # Mark all the vertices
        # as not visited
        visited = [False] * len(self.nodes)

        # Call the recursive helper
        # function to print all paths
        pathCount = [0]
        self.countPathsUtil(s, d, visited, pathCount)
        return pathCount[0]

        # A recursive function to print all paths

    # from 'u' to 'd'. visited[] keeps track
    # of vertices in current path. path[]
    # stores actual vertices and path_index
    # is current index in path[]
    def countPathsUtil(self, u, d,
                       visited, pathCount):
        visited[u] = True

        # If current vertex is same as
        # destination, then increment count
        if (u == d):
            pathCount[0] += 1

        # If current vertex is not destination
        else:

            # Recur for all the vertices
            # adjacent to current vertex
            i = 0
            while i < len(self.adj_list[u]):
                if (not visited[self.adj_list[u][i]]):
                    self.countPathsUtil(self.adj_list[u][i], d,
                                        visited, pathCount)
                i += 1

        visited[u] = False


if __name__ == "__main__":
        # Create a graph given in the
        # above diagram
        V = [0,1,2,3]
        g = Graph(V)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(0, 3)
        g.addEdge(2, 0)
        g.addEdge(2, 1)
        g.addEdge(1, 3)
        g.print_adj_list()

        s = 2
        d = 3
        print(g.countPaths(s, d))
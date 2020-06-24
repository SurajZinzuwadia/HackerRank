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


    def BFS(self):
        u = 0
        temp = []
        for i in range(0,36):
            x = max(self.adj_list[u])
            temp.append(u)
            if x ==36:
                break
            u = x
        print(temp)


if __name__ == "__main__":
    V = [i for i in range(0,37)]
    graph = Graph(V)
    board = [0] * 50
    board[2] = 13
    board[5] = 2
    board[9] = 18
    board[18] = 11
    board[17] = -13
    board[20] = -14
    board[24] = -8
    board[25] = -10
    board[32] = -2
    board[34] = -22
    for u in range(0,36):
        for dice in range(1,7):
                v = u + dice + board[u+dice]
                if v<=36:
                    graph.add_edge(u,v)
    print(graph.print_adj_list())
    graph.BFS()

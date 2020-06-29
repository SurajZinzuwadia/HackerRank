#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
# class Graph:
#     def __init__(self,Nodes, is_directed = False):
#         self.nodes = Nodes
#         self.adj_list = {}
#         self.is_directed = is_directed
#         for node in range(1,self.nodes+1):
#             self.adj_list[node] = []
#
#     def add_edge(self,u,v):
#         self.adj_list[u].append(v)
#         # if not self.is_directed:
#         #     self.adj_list[v].append(u)
#
#     def DFS(self,s):
#         visited = {}
#         stack = []
#         dfs_output = []
#         for node in self.adj_list.keys():
#             visited[node] = False
#         s = s
#         visited[s] = True
#         stack.append(s)
#         while len(stack)!=0:
#             # print(stack)
#             u = stack.pop()
#             dfs_output.append(u)
#             for v in self.adj_list[u]:
#                 if not visited[v]:
#                     visited[v] = True
#                     stack.append(v)
#         return (dfs_output
#         )
#
#
#     def roadsAndLibraries(self,n, c_lib, c_road, cities):
#         queue = []
#         for i in range(1,n+1):
#             queue.append(i)
#         result = c_lib
#
#         if(c_lib < c_road):
#             result = result  + c_lib*(n-1)
#         else:
#             while len(queue)!=0:
#                 s = queue[0]
#                 dfs = self.DFS(s)
#                 # print("dfs",dfs)
#                 length = len(dfs)
#                 if ( length == 1):
#                     result = result + c_lib
#                 else:
#                     result = result  + (length-1)*c_road
#                 for i in dfs:
#                     # print(i)
#                     # print(queue)
#                     queue.remove(i)
#         return result

def roadsAndLibraries(n, c_lib, c_road, cities):
    total = 0
    if c_lib < c_road:
        total = n * c_lib
    else:
        neighbours = {}
        visited = [False] * n
        connectedComponents = 0
        nodes_per_cluster = {}

        # recursive DFS
        def dfs(i, cluster):
            if not visited[i]:
                # check how many unique nodes are in this cluster
                nodes_per_cluster[cluster] = (
                        nodes_per_cluster.get(cluster, 0) + 1)
            # mark this as visited
            visited[i] = True
            my_neighbours = []
            try:
                my_neighbours = neighbours[i + 1]
            except KeyError as ke:
                # we found a single node cluster (city with one house)
                # leave the list empty and the for-loop will skip it
                pass
            for city_id in my_neighbours:
                if not visited[city_id - 1]:
                    dfs(city_id - 1, cluster)

        # populate the adjacency list
        for road in cities:
            neighbours[road[0]] = (
                    neighbours.get(road[0], []) + [road[1]])
            neighbours[road[1]] = (
                    neighbours.get(road[1], []) + [road[0]])

        for i in range(n):
            if not visited[i]:
                dfs(i, i)
                connectedComponents += 1

        # min number of roads is always number of houses - 1
        roads = sum(x - 1 for x in nodes_per_cluster.values())

        total = c_road * roads + c_lib * connectedComponents
    return total
if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0]) # number of cities
        graph = Graph(n)
        m = int(nmC_libC_road[1]) # number of roads

        c_lib = int(nmC_libC_road[2]) # price of lib

        c_road = int(nmC_libC_road[3]) # price of city

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))
        # print(cities)
        for u,v in cities:
            graph.add_edge(u,v)
        result = graph.roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)
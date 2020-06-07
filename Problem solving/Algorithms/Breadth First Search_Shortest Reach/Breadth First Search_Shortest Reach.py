#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
from collections import defaultdict , deque
def creategraph(edges, m):
    d = defaultdict(set)
    for i in range(m):
        u, v = edges[i][0], edges[i][1]
        d[u].add(v)
        d[v].add(u)
    return d


def bfs(n, m, edges, s):
    d = creategraph(edges, m)
    visited = [False] * (n + 1)
    distance = [-1] * (n + 1)
    q = deque()
    q.appendleft(s)
    level = 0
    while q:
        l = len(q)
        for i in range(l):
            p = q.pop()
            if distance[p] == -1:
                distance[p] = level * 6
            visited[p] = True
            for node in d[p]:
                if not visited[node]:
                    q.appendleft(node)
        level += 1
    distance.remove(0)
    return distance[1:]
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)
        print(result)

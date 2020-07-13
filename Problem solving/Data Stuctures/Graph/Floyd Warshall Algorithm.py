import math
import os
import random
import re
import sys



def floyed(n,dist):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])



if __name__ == '__main__':
    n, m = map(int, input().strip().split(" "))
    dist = [[math.inf] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        i,j,w=map(int,input().strip().split(" "))
        dist[i][j]=w
    for i in range(1,n+1):
        dist[i][i]=0
    floyed(n,dist)
    q=int(input())

    for _ in range(q):
        i, j=map(int, input().strip().split(" "))
        print(dist[i][j] if dist[i][j]!=math.inf else -1)

#other way
# from itertools import product
# INF = 999
# def floyd_warshall(N,temp,temp1):
#     dist = [[INF]*N for i in range(N)]
#     nxt = [[0] * N for i in range(N)]
#     for i in range(N):
#         dist[i][i] = 0
#     for u,v,w in temp:
#         dist[u-1][v-1] = w
#         nxt[u - 1][v - 1] = v - 1
#     for k, i, j in product(range(N), repeat=3):
#         sum_ik_kj = dist[i][k] + dist[k][j]
#         if dist[i][j] > sum_ik_kj:
#             dist[i][j] = sum_ik_kj
#             nxt[i][j] = nxt[i][k]
#     for i,j in temp1:
#         if(dist[i-1][j-1] == 999):
#             print(-1)
#         else:
#             print(dist[i-1][j-1])
#
# if __name__ == '__main__':
#     nN = input().strip().split()
#     N = int(nN[1])
#     temp = []
#     for i in range(N):
#         temp.append(list(map(int,input().strip().split())))
#     x = int(input())
#     temp1 = []
#     for i in range(x):
#         temp1.append(list(map(int,input().strip().split())))
#     floyd_warshall(N,temp,temp1)



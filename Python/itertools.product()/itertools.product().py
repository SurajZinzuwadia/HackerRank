from itertools import product
n = input().split()
n = list(map(int,n))
m = input().split()
m = list(map(int,m))
print(*product(n,m))

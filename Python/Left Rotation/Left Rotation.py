n, d = map(int, input().split())
result = [0] * n
a = list(map(int, input().rstrip().split()))
ans = []
result = [0] * n
for i in range(0,n):
    result[(i+n-d)%n] = a[i]
print(*result, sep=" ")

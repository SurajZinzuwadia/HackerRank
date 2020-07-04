def find_set(x, sets):
    if sets[x] < 0:
        return x
    else:
        sets[x] = find_set(sets[x], sets)
        return sets[x]

def union_set(u, v, sets):
    a = find_set(u, sets)
    b = find_set(v, sets)

    newSize = sets[a] + sets[b]

    if sets[a] > sets[b]:
        sets[a] = b
        sets[b] = newSize
    else:
        sets[b] = a
        sets[a] = newSize

n, p = map(int, input().split())
sets = [-1 for _ in range(n)]

for _ in range(p):
    u, v = map(int, input().split())
    set_u = find_set(u, sets)
    set_v = find_set(v, sets)

    if set_u != set_v:
        union_set(set_u, set_v, sets)

l = [0] * n
for i in range(n):
    if sets[i] < 0:
        l[i] += 1
    else:
        l[find_set(sets[i], sets)] += 1

summ = 0
ans = 0
for i in l:
    ans += i * summ
    summ += i
print(ans)
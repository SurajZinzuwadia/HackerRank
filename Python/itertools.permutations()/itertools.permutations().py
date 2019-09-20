from itertools import permutations
S, part = input().split()
r =list(permutations(S,int(part)))
r.sort()
for i in r:
    print(''.join(i))

from itertools import combinations_with_replacement
S, part = input().split()
r = list(combinations_with_replacement(sorted(S),int(part)))
for i in r:
    print(''.join(i))

from itertools import permutations

s,k = input().split()

print(*[''.join(i) for i in permutations(sorted(s),int(k))],sep='\n')

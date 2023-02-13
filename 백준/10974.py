import sys
from itertools import permutations
sys.stdin = open("10974.txt", "r")

n=int(input())
s=[]
for i in range(1,n+1):
    s.append(i)
z=list(permutations(s,n))#중복 0
for i in z:
    print(*i)
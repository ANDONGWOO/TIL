import sys
from itertools import permutations
sys.stdin = open("15649.txt", "r")

n,m= map(int,input().split())
q=[]
for i in range(1,n+1):
    q.append(i)
s=list(permutations(q,m))#중복o
for i in s:
    print(*i)
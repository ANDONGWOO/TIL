import sys
from itertools import combinations
sys.stdin = open("15650.txt", "r")

n,m= map(int,input().split())
q=[]
for i in range(1,n+1):
    q.append(i)
s=list(combinations(q,m))#중복x
for i in s:
    print(*i)
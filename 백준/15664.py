import sys
from itertools import  combinations
sys.stdin = open("15664.txt", "r")

n,m= map(int,input().split())
q=list(map(int,input().split()))
q.sort()
s=list(set(combinations(q, m)))
s.sort()
for i in s:
    print(' '.join(map(str,i)))
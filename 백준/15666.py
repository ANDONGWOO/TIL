import sys
from itertools import  combinations_with_replacement
sys.stdin = open("15666.txt", "r")

n,m= map(int,input().split())
q=list(map(int,input().split()))
q.sort()
s=list(set(combinations_with_replacement(q,m)))
s.sort()
for i in s:
    print(' '.join(map(str,i)))
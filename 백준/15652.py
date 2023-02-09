import sys
from itertools import combinations_with_replacement
sys.stdin = open("15652.txt", "r")

n,m= map(int,input().split())
q=list(range(1,n+1))
s=list(combinations_with_replacement(q, m))
for i in s:
    print(' '.join(map(str,i)))

import sys
from itertools import  permutations
sys.stdin = open("15663.txt", "r")

n,m= map(int,input().split())
q=list(map(int,input().split()))
s=list(set(permutations(q, m)))
s.sort()
for i in s:
    print(' '.join(map(str,i)))
import sys
from itertools import permutations
sys.stdin = open("15654.txt", "r")

n,m= map(int,input().split())
q=list(map(int,input().split()))
s=list(permutations(q, m))
s.sort()#사전순으로 
for i in s:
    print(' '.join(map(str,i)))

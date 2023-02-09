import sys
from itertools import product
sys.stdin = open("15651.txt", "r")

n,m= map(int,input().split())
q=list(range(1,n+1))
s=list(product(q, repeat=m))
for i in s:
    print(' '.join(map(str,i)))

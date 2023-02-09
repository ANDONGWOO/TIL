import sys
from itertools import  product
sys.stdin = open("15665.txt", "r")

n,m= map(int,input().split())
q=list(map(int,input().split()))

s=list(set(product(q, repeat=m)))
s.sort()
for i in s:
    print(' '.join(map(str,i)))
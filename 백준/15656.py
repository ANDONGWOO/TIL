import sys
from itertools import  product
sys.stdin = open("15656.txt", "r")

n,m= map(int,input().split())
q=list(map(int,input().split()))
q.sort()
s=list(product(q, repeat=m))

for i in s:
    print(' '.join(map(str,i)))
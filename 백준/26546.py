import sys
import re
sys.stdin = open("26546.txt", "r")

t=int(input())

for _ in range(t):
    a,b,c=map(str, input().split())
    q=a
    w = re.sub(q[int(b):int(c)], '', q)#정규식
    print(w)
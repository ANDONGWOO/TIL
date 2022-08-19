import sys

sys.stdin = open("25304.txt", "r")

x=int(input())
n=int(input())
s=0
q=0
for i in range(n):
    a,b=map(int,input().split())
    if q!=n:
        q+=1
        s+=(a*b)
        if q==n and s==x:
            print('Yes')
        if  q==n and s!=x:
            print('No')

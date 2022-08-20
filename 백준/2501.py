import sys

sys.stdin = open("2501.txt", "r")

n,k=map(int,input().split())
s=0
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
        s+=1
if s<k:
    print(0)
if s>=k:
    print(a[k-1])
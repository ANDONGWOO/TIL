import sys
sys.stdin = open("5032.txt", "r")

a,b,c=map(int,input().split())
s=a+b
q=0

while s>=c:
    s=s-c
    q+=1
    s+=1
print(q)
import sys
sys.stdin = open("4299.txt", "r")

a,b=map(int,input().split())

if a-b<0 or (a-b)%2!=0:
    print(-1)
else:
    c=(a-b)//2
    d=a-c
    print(max(c,d),min(c,d))


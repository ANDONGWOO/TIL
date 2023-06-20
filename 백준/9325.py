import sys
sys.stdin = open("9325.txt", "r")

t=int(input())
s=0
for _ in range(t):
    s=int(input())
    q=int(input())#서로다른 옵션 개수
    for i in range(q):
        a,b=map(int,input().split())
        s+=a*b
    print(s)

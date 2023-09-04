import sys

sys.stdin = open("11098.txt", "r")

n=int(input())
for _ in range(n):
    p=int(input())
    m=0
    s=""
    for _ in range(p):
        a,b=input().split()
        if m<int(a):
            m=int(a)
            s=b
    print(s)
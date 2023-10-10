import sys

sys.stdin = open("30007.txt", "r")

t=int(input())

for _ in range(t):
    a,b,x=map(int,input().split())
    print(a*(x-1)+b)
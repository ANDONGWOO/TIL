import sys

sys.stdin = open("11312.txt", "r")

t=int(input())

for _ in range(t):
    a,b=map(int,input().split())
    print((a//b)**2)
import sys
sys.stdin = open("9093.txt", "r")

t=int(input())

for i in range(t):
    a=list(input().split())
    for k in a:
        print(k[::-1], end=" ")
import sys
sys.stdin = open("4562.txt", "r")

t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    if a==b or a>b:
        print('MMM BRAINS')
    else:
        print('NO BRAINS')
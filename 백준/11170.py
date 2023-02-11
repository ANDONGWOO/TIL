import sys

sys.stdin = open("11170.txt", "r")

n=int(input())
for i in range(n):
    x=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        x+=str(j).count('0')
    print(x)
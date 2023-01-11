import sys

sys.stdin = open("1312.txt", "r")

a,b,c=map(int,input().split())

for i in range(c):
    a=(a%b*10)
    q=a//b
print(q)
import sys

sys.stdin = open("2738.txt", "r")
input=sys.stdin.readline
n,m=map(int,input().split())

q=[list(map(int,input().split()))for _ in range(n)]
w=[list(map(int,input().split()))for _ in range(n)]
s=[]
for i in range(n):
    for j in range(m):
        q[i][j]+=w[i][j]

for i in q:
    print(*i)
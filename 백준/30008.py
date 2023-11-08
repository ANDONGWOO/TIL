import sys

sys.stdin = open("30008.txt", "r")


n,k=map(int,input().split())
g=list(map(int,input().split()))
q=[]
for i in range(k):
    if 0<=g[i]<=4:
        q.append(1)
    if 4<=g[i]<=11:
        q.append(2)
    if 11<=g[i]<=23:
        q.append(3)
    if 23<=g[i]<=40:
        q.append(4)
    if 40<=g[i]<=60:
        q.append(5)
    if 60<=g[i]<=77:
        q.append(6)
    if 77<=g[i]<=89:
        q.append(7)
    if 89<=g[i]<=96:
        q.append(8)
    if 96<=g[i]<=100:
        q.append(9)
print(q)
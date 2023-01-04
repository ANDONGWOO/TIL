import sys

sys.stdin = open("10825.txt", "r")

t=int(input())
q=[]
for _ in range(t):
    q.append(input().split())
q.sort(key= lambda x:(-int(x[1]),int(x[2]),-int(x[3]), x[0]))

for j in q:
    print(j[0])
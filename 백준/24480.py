
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("24480.txt", "r")
input = sys.stdin.readline

n,m,r=map(int,input().split())
graph=[[]for _ in range(n+1)]
visited=[0] * (n+1)
s=1

for _ in range(m):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in graph:
    i.sort(reverse=True)

def dfs(v):
    global s
    visited[v]=s
    for adj in graph[v]:
        if visited[adj]:
            continue
        s+=1
        dfs(adj)
dfs(r)
for i in visited[1:]:
    print(i)

import sys
from collections import deque
sys.stdin = open("1260.txt", "r")


n,m,v=map(int,input().split())
graph=[[]for _ in range(n+1)]


for _ in range(m):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    graph[v1].sort()
    graph[v2].sort()


visited=[False] * (n+1)

def dfs(graph, v, visited):
    visited[v]=True
    print(v,end=' ')
    for adj in graph[v]:
        if not visited[adj]:
            dfs(graph, adj, visited)


def bfs(graph, v, visited):
    visited=[False] * (n+1)
    queue= deque([v])
    visited[v] =True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for j in graph[v]:
            if not visited[j]:
                queue.append(j)
                visited[j]=True

dfs(graph, v, visited)
print()
bfs(graph, v, visited)




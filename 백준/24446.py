from collections import deque
import sys
sys.stdin = open("24446.txt", "r")
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    q = deque([r])
    visited[r] = 0 #방문 0으로 
    while q:
        v = q.popleft()
        for g in graph[v]:
            if visited[g] == -1:#방문 x이면
                visited[g] = visited[v]+1
                q.append(g)
bfs(r)#시작점

for v in visited[1:]:
    print(v)
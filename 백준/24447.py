from collections import deque
import sys
sys.stdin = open("24447.txt", "r")
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [[-1, 0] for _ in range(n + 1)]
s=1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global s
    q = deque([r])
    visited[r][0] = 0
    while q:
        v = q.popleft()
        for g in graph[v]:
            if visited[g][0] == -1:
                s+=1
                visited[g] = visited[v][0]+1 ,s
                q.append(g)
bfs(r)#시작점
z=0
for i in graph:
    i.sort(reverse=True)
for v in visited:
    z+= v[0]*v[1]
print(z)
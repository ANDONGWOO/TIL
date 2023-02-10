import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("24482.txt", "r")
input = sys.stdin.readline

n,m,r=map(int,input().split())
graph =[[]for _ in range(n+1)]
visited=[-1]*(n+1)

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = visited[v]+1
            dfs(i)

visited[r] = 0
dfs(r)

for j in visited[1:]:
    print(j)
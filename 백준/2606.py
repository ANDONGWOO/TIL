import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("2606.txt", "r")
input = sys.stdin.readline

n=int(input())
m=int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
s=0
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    global s
    visited[v]= True#방문하면
    for i in graph[v]:#graph요소 i
        if visited[i]==False:
            visited[i]=True
            s+=1
            dfs(i)

for i in range(1,n+1):
    if visited[i]==False:#방문X
        dfs(1)#시작점
print(s)
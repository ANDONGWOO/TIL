import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("11724.txt", "r")
input = sys.stdin.readline

n,m=map(int,input().split())
graph =[[]for _ in range(n+1)]
visited=[False]*(n+1)
s=0
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
def dfs(v):
    visited[v]=True#방문하면 True
    for i in graph[v]:#graph요소 i
        if visited[i]== False:#True이면 다시반복
            visited[i]==True
            dfs(i)

for i in range(1,n+1):
    if visited[i]==False:
        s+=1#처음 +1 전체돌고 +1
        dfs(i)#시작점
print(s)

#문제 그래프 수 출력
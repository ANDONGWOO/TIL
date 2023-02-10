import sys
sys.setrecursionlimit(10 ** 8)
sys.stdin = open("24484.txt", "r")
input = sys.stdin.readline

n,m,r=map(int,input().split())
graph =[[]for _ in range(n+1)]
visited=[-1 for _ in range(n+1)]
s=1
s_list=[0 for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in graph:
    i.sort(reverse=True)

def dfs(v,z):
    global s
    visited[v]=z
    s_list[v]=s
    for i in graph[v]:
        if visited[i] == -1:
            s+=1
            dfs(i,z+1)

dfs(r,0)#처음 값
x=0#총합
for j in range(1,n+1):
    x+=s_list[j]*visited[j]
print(x)
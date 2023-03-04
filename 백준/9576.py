import sys
sys.stdin = open("9576.txt", "r")

input = sys.stdin.readline
t=int(input())
def dfs(v):
    if visited[v]:

        return False
    visited[v] = True
    for z in graph[v]:
 
        if not matching_list[z] or dfs(matching_list[z]):

            matching_list[z] = v
            return True
            
    return False
for i in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(m+1)]
    matching_list = [0 for _ in range(n+1)]
    s=0
    for k in range(1, m+1):
        a,b = map(int, input().split())
        for j in range(a,b+1):
            graph[k].append(j)  
    for j in range(1, m+1):
        visited = [False for _ in range(m+1)]
        if dfs(j):
            s+=1
    print(s) 
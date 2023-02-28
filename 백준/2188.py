import sys
sys.stdin = open("2188.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
matching_list = [0 for _ in range(m+1)]
for g in range(1, n+1):
    array = list(map(int, input().split()))
    for j in array[1:]:
        graph[g].append(j)

def dfs(v):
    if visited[v]:#방문여부
        return False
    visited[v] = True#방문 체크
    for z in graph[v]:
        if not matching_list[z] or dfs(matching_list[z]):
            matching_list[z] = v
            return True      
    return False

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]#방문여부
    dfs(i)
print(len([1 for i in matching_list if i > 0]))
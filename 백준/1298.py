import sys
sys.stdin = open("1298.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
matching_list = [0 for _ in range(n+1)]
s=0
for k in range(m):#노트북 예상의 개수
    a, b = map(int, input().split())
    graph[a].append(b)#graph[a]에  b추가
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
    if dfs(i):#시작점
        s+=1
print(s)

import sys
sys.stdin = open("11375.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]#일번호의 목록
matching_list = [0 for _ in range(m+1)]#매칭의 목록

for i in range(1, n+1):
    array = list(map(int, input().split()))#일의목록
    for j in array[1:]:#각줄의 일번호
        graph[i].append(j)
        
def dfs(v):
    if visited[v]:
        return False
    visited[v] = True
    
    for i in graph[v]:
        if not matching_list[i] or dfs(matching_list[i]):
            matching_list[i] = v
            return True
            
    return False

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    dfs(i)#시작점
# print(visited)TRUE이면 매칭X
print(len([1 for i in matching_list if i > 0]))#일의 수

#둘째줄 부터 각줄에는 일 수, 할수있는일의 번호
#pypy3제출
#직원 최대 일 1
import sys
sys.stdin = open("11377.txt", "r")
input = sys.stdin.readline

n, m ,k  = map(int, input().split())
graph = [[] for _ in range(n+1)]#일번호의 목록
matching_list = [0 for _ in range(m+1)]#매칭의 목록
s=0#일의 개수
for g in range(1, n+1):#1~n까지
    array = list(map(int, input().split()))#일의목록
    for j in array[1:]:#각줄의 일번호
        graph[g].append(j)
def dfs(v):
    if visited[v]:#방문여부
        return False
    visited[v] = True#방문 체크
    for z in graph[v]:
        if not matching_list[z] or dfs(matching_list[z]):#3/1
            matching_list[z] = v
            return True
            
    return False
x=0
for j in range(2):
    x+=1
    for i in range(1, n+1):
        visited = [False for _ in range(n+1)]#방문여부
        if dfs(i):
            s+=1#일의 개수
            if x==2:#dfs 두번째라면
                k-=1
                if k==0:
                    break            
print(s)#일의 개수
#dfs 두번돌려서 직업한명이 두가지 일 선택
#그래서 k가 0이면 종료 
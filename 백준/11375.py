
import sys
sys.stdin = open("11375.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]#일번호의 목록
matching_list = [0 for _ in range(m+1)]#매칭의 목록
# print(matching_list[0])
for k in range(1, n+1):#1~n까지
    array = list(map(int, input().split()))#일의목록
    for j in array[1:]:#각줄의 일번호
        graph[k].append(j)
        #print(array[1:])
        #print(j)일번호 나열 1,2,/1,/2,3,/3,4,5,/1
#print(graph)graph[1~n까지][1, 2], [1], [2, 3], [3, 4, 5], [1]    
def dfs(v):
    if visited[v]:
        # print(visited[v])
        return False
    visited[v] = True
    # print(graph[v])
    for z in graph[v]:#graph[1~n까지][1, 2], [1], [2, 3], [3, 4, 5], [1]
        # print(z)
        if not matching_list[z] or dfs(matching_list[z]):#3/1
            # print(not matching_list[z])True,True,False,True,True/ 4 TRUE
            # print(dfs(matching_list[z]))False,False,False,False,False/ 0 TRUE
            # if T4/F1
            # matching_list[z]
            #[1, 2], [1], [2, 3], [3, 4, 5], [1]그림
            #print(v)#1,1,2,3,4,4
            matching_list[z] = v#1,1,2,3,4,4
            print(matching_list[z])
            return True
            
    return False

for i in range(1, n+1):#1~n까지
    visited = [False for _ in range(n+1)]
    dfs(i)#시작점
print(visited)#TRUE이면 매칭X
# print(matching_list)#[0, 2, 1, 3, 4, 0]그림 결과
# print([1 for i in matching_list if i > 0])#[1, 1, 1, 1]
print(len([1 for i in matching_list if i > 0]))#일의 수 matching_list 반복문 돌리고 IF I>0 1 그래서 답4 

#둘째줄 부터 각줄에는 일 수, 할수있는일의 번호
#pypy3제출
#직원 최대 일 1

#직원과 일
#용량 1 
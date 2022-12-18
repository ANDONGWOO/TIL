import sys

sys.stdin = open("25305.txt", "r")

T,Q =map(int,input().split())#T응시자의 수/Q 상을 받는 사람의 수

s=list(map(int,input().split()))
s.sort()#정렬 하고 
for i in range(1,Q+1):#상을 받는 사람의 수 반복돌려서 w에서 추가
    w=[]
    w.append(s.pop())
print(*w)

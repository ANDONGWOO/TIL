import sys
sys.stdin = open("3047.txt", "r")


q=list(map(int,input().split()))
w=list(input())
q.sort()
for i in w:
    if i == "A":#무조건 제일 작은수
        print(q[0], end=" ") 
    elif i == "B":#무조건 중간 나오고
        print(q[1], end=" ")
    else:
        print(q[2], end=" ")#제일 큰수
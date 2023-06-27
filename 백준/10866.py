import sys
from collections import deque
sys.stdin = open("10866.txt", "r")


t=int(input())

w=deque()
for i in range(t):
    q=list(map(str,sys.stdin.readline().split()))
    if q[0]=="push_front":
        w.appendleft(q[1])#덱의 앞에 넣는다
    elif q[0]=="push_back":
        w.append(q[1])#덱의 뒤에 넣는다
    elif q[0]=="pop_front":
        if len(w)>=1:
            print(w.popleft())#맨 앞의 정수를 빼고
        else:
            print(-1)
    elif q[0]=="pop_back":
        if len(w)>=1:
            print(w.pop())#맨 뒤의 정수를 빼고
        else:
            print(-1)
    elif q[0]=="size":
        print(len(w))
    elif q[0]=="empty":
        if len(w)==0:
            print(1)
        else:
            print(0)
    elif q[0]=="front":
        if len(w)>=1:
            print(w[0])
        else:
            print(-1)
    else:
        if len(w)>=1:
            print(w[-1])
        else:
            print(-1)
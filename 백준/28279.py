import sys
from collections import deque
sys.stdin = open("28279.txt", "r")


t=int(sys.stdin.readline())
w=deque()
for i in range(t):
    q=list(map(int,sys.stdin.readline().split()))
    if q[0]==1:
        w.appendleft(q[1])#덱의 앞에 넣는다
    elif q[0]==2:
        w.append(q[1])#덱의 뒤에 넣는다
    elif q[0]==3:
        if len(w)>=1:
            print(w.popleft())#맨 앞의 정수를 빼고
        else:
            print(-1)
    elif q[0]==4:
        if len(w)>=1:
            print(w.pop())#맨 뒤의 정수를 빼고
        else:
            print(-1)
    elif q[0]==5:
        print(len(w))
    elif q[0]==6:
        if len(w)==0:
            print(1)
        else:
            print(0)
    elif q[0]==7:
        if len(w)>=1:
            print(w[0])
        else:
            print(-1)
    else:
        if len(w)>=1:
            print(w[-1])
        else:
            print(-1)

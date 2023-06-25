import sys

sys.stdin = open("28278.txt", "r")

t=int(sys.stdin.readline())
stack=[]
for i in range(t):
    q=list(map(int,sys.stdin.readline().split()))
    if q[0]==1:
        stack.append(q[1])
    elif q[0]==2:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif q[0]==3:
        print(len(stack))
    elif q[0]==4:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
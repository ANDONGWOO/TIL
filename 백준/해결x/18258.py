import sys
import queue
sys.stdin = open("18258.txt", "r")

n=int(sys.stdin.readline())

queue=[]
for i in range(n):
    s=sys.stdin.readline().split()
    w=s[0]
    if w=='push':
        queue.insert(0,s[1])
    elif w=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop())       
    elif w=='size':
        print(len(queue))
    elif w=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif w=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[len(queue) -1])
    elif w=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
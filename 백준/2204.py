import sys
sys.stdin = open("2204.txt", "r")


while 1:
    t=int(input())
    if t==0:
        break
    else:
        q=[]
        for i in range(t):
            q.append(input())
        q.sort(key=str.lower)
        print(q[0])

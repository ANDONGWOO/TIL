import sys

sys.stdin = open("1485.txt", "r")

t=int(input())
for _ in range(t):
    q=[]
    s=0
    for i in range(4):
        a,b=map(int,input().split())
        q.append([a,b])
        if a==b:
            s+=1
        w=sorted(q)
    if s==4:
        print(0)
        break
    elif w[0][0]==w[0][1] and w[0][0]==w[1][0] and w[0][0]==w[2][1] and w[3][0]==w[3][1] and w[3][0]==w[2][0] and w[3][0]==w[1][1]:
        print(1)
    else:
        print(0)
import sys
sys.stdin = open("9506.txt", "r")

input= sys.stdin.readline

while 1:
    s=int(input())
    if s==-1:
        break
    q=[]
    for i in range(1,s):
        if s%i==0:
            q.append(i)
    if sum(q)==s:
        print(s,"=",end=" ")
        print(*q, sep=" + ")
    else:
        print(s, 'is NOT perfect.')
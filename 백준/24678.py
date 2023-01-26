import sys

sys.stdin = open("24678.txt", "r")
input=sys.stdin.readline
t=int(input())

for i in range(t):#테스트케이스
    q=0
    w=0
    z=list(map(int,input().split()))
    for j in range(3):#돌무더기3
        if z[j] % 2 != 0:
            q+=1
        else:
            w+=1
    if w==3 or w==2:
        print('R')
    else:
        print('B')
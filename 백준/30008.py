import sys

sys.stdin = open("30008.txt", "r")


n,k=map(int,input().split())
g=list(map(int,input().split()))
q=[]

w=0
for i in range(k):
    w=(g[i]*100)//n
    if 0<=w<=4:
        q=1
    elif 4<=w<=11:
        q=2
    elif 11<=w<=23:
        q=3
    elif 23<=w<=40:
        q=4
    elif 40<=w<=60:
        q=5
    elif 60<=w<=77:
        q=6
    elif 77<=w<=89:
        q=7
    elif 89<=w<=96:
        q=8
    elif 96<=w<=100:
        q=9
    print(q,end=" ")
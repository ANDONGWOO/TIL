import sys

sys.stdin = open("28289.txt", "r")

p=int(input())

q=0
w=0
e=0
r=0
for _ in range(p):
    g,c,n=map(int,input().split())
    if g==1:
        r+=1
    elif (g==2 or g==3) and (c==1 or c==2):
        q+=1
    elif (g==2 or g==3) and c==3:
        w+=1
    elif(g==2 or g==3) and c==4:
        e+=1
print(q,w,e,r,sep="\n")
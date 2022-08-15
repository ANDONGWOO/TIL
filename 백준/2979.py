import sys

sys.stdin = open("2979.txt", "r")

A,B,C=map(int,input().split())


r=[list(map(int,input().split())) for _ in range(3)]
n=max(r[0][1],r[1][1],r[2][1])
a=[0]*(n-1)
for q in r:
    for  i in range(q[0]-1,q[1]-1):
        a[i]=a[i]+1
        b=0
        for w in a:
            if w ==1:
                b=b+A
            elif w ==2:
                 b=b+2*B
            elif w ==3:
                 b=b+3*C
print(b)

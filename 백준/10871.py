import sys
sys.stdin = open("10871.txt", "r")

N,X=map(int,input().split())

T=list(map(int,input().split()))
a=[]
for i in T:
    if i<X:
        a=i
        print(a,end=" ")

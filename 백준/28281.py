import sys

sys.stdin = open("28281.txt", "r")

n,x=map(int,input().split())
q=list(map(int,input().split()))
w=[]
for i in range(1,n):#1시작 
    w.append(q[i-1]*x+q[i]*x)#시작 0인덱스/1인덱스
print(min(w))
import sys
sys.stdin = open("10865.txt", "r")

n,m=map(int,sys.stdin.readline().split())
q=[0]*(n+1)
for i in range(m):#친구 관계 a,b
    a,b=map(int,sys.stdin.readline().split())
    q[a]+=1
    q[b]+=1
print(*q[1::],sep="\n")
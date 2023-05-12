import sys

sys.stdin = open("1547.txt", "r")

n=int(input())
q=[1,2,3]
for _ in range(n):
    a,b=map(int,input().split())
    a1=q.index(a)
    b2=q.index(b)
    q[a1],q[b2]=q[b2],q[a1]
print(q[0])
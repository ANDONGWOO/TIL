import sys
sys.stdin = open("10810.txt", "r")


n,m=map(int,input().split())

q=[0]*n
for i in range(m):
    a,b,c=map(int,input().split())
    for i in range(a-1,b):#a-1 인덱스번호로 동일
        q[i]=c
print(*q)

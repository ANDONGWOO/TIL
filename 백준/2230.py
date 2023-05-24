import sys
sys.stdin = open("2230.txt", "r")

n,m=map(int,sys.stdin.readline().split())
q=[]


for i in range(n):
    q.append(int(input()))
q.sort()
a,b=0,1
e=21474836647
while a<n and b<n:
    w=q[b]-q[a]
    if w==m:
        print(m)
        sys.exit(0)#종료0 강제종료1
    if w<m:
        b+=1
        continue#아래 실행x
    a+=1
    e=min(e,w)

print(e)

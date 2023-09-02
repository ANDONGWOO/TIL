import sys
sys.stdin = open("20112.txt", "r")

n=int(input())
q=[]
for i in range(n):
    s=list(input())
    q.append(s)
    s=0
for j in range(n):
    if q[j][0]==q[0][j] and q[j][n-1]==q[n-1][j]:#가로세로확인
        s+=1
    else:
        print("NO")
        sys.exit(0)
if s==n:
    print("YES")
else:
    print("NO")

import sys
sys.stdin = open("3009.txt", "r")

A=[]
B=[]


for i in range(3):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
q=[]
if A[0]==A[1]:
    q.append(A[-1])
else:
    q.append(A[0])
if B[0]==B[1]:
    q.append(B[-1])
else:
    q.append(B[0])
print(*q)
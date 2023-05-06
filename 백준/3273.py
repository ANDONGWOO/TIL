import sys
input = sys.stdin.readline
sys.stdin = open("3273.txt", "r")

n=int(input())

q=list(map(int,input().split()))

w=int(input())
s=0
q.sort()

for i in range(n):
    for j in range(i+1,n):
        if q[i]+q[j]==w:#시작이 0인덱스, 1인덱스  
            s+=1
        elif q[i]+q[j]>w:
            break
print(s)

#PyPy3
import sys
sys.stdin = open("28014.txt", "r")

t=int(input())
q=list(map(int,input().split()))
s=1
for i in range(1,t):
    if q[i]>=q[i-1]:
        s+=1
print(s)
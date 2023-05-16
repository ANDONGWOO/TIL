import sys

sys.stdin = open("2506.txt", "r")


t=int(input())
a,b=0,0
s=list(map(int,input().split()))
for j in range(t):
    if s[j]==1:
        a+=1
        b+=a
    else:
        a=0
print(b)
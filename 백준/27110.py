import sys

sys.stdin = open("27110.txt", "r")

t=int(input())

q= list(map(int,input().split()))
s=0
for i in range(3):
    if q[i]>=t:
        s+=t
    else:
        s+=q[i]
print(s)
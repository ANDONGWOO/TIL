import sys

sys.stdin = open("26068.txt", "r")


t=int(input())
s=0
for i in range(t):
    q=input()
    if int(q[2:])<=90:#90이하
        s+=1
print(s)
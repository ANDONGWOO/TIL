import sys
sys.stdin = open("7567.txt", "r")

q=list(input())

s=0

for i in range(len(q)):
    if i==0 or q[i]!=q[i-1]:
        s+=10
    else :
        s+=5
print(s)
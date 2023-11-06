import sys
sys.stdin = open("30486.txt", "r")

s,d,i,l,n=map(int, input().split())
q=s+d+i+l
s=0
while 1:
    if q/4>=n:
        break
    else:
        q+=1
        s+=1
print(s)
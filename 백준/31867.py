import sys
sys.stdin = open("31867.txt", "r")


n=int(input())
k=list(map(int,input()))
s1=0
s2=0

for i in range(n):
    if k[i]%2==0:
        s1+=1
    else:
        s2+=1
if s1>s2:
    print(0)
elif s1<s2:
    print(1)
else:
    print(-1)
import sys

sys.stdin = open("28352.txt", "r")

t=int(input())
s=1
if t>0:
    for i in range(1,t+1):
        s *= i

s/=3600#시
s/=24#일
s/=7#주
print(int(s))

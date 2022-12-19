import sys

sys.stdin = open("2455.txt", "r")

t=0
s=[]
for i in range(1,4+1):#역수
    a,b=map(int, input().split())
    t-=a#내린 사람 수 
    t+=b#탄 사람 수
    s.append(t)
print(max(s))
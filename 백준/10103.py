import sys

sys.stdin = open("10103.txt", "r")

T=int(input())
c=100#창영점수
s=100#상덕점수
for i in range(1,T+1):
    a,b=map(int,input().split())#게임 당 a는 창영 주사위수,b는 상덕 주사위수
    if a<b:
        c=c-b#창영점수 - 상덕 주사위수
    if a>b:
        s=s-a#상덕점수 - 창영 주사위수
    else:
        continue
print(c)
print(s)
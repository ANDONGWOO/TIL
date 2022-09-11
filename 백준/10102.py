import sys

sys.stdin = open("10102.txt", "r")

s=int(input())#투표수
q=list(input())#투표결과
e=0#A득표
r=0#B득표
for i in range(s):
    if q[i]=='A':#A 동일하다면
        e+=1
    elif q[i]=='B':#B 동일하다면
        r+=1

if e>r:#e가 크다면 A출력
    print('A')
elif e<r:#e가 작다면 B출력
    print('B')
elif r==e:#동일하다면 Tie
    print('Tie')
     

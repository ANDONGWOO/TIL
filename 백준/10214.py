import sys

sys.stdin = open("10214.txt", "r")

T=int(input())#케이스 수
y=0#연세대
k=0#고려대대
for i in range(1,T+1):
    for j in range(1,9):
        a,b=map(int,input().split())
        y+=a
        k+=b
    if y==k:
        print("Draw")
    elif y>k:#y크다면
        print("Yonsei")
    else:#k크다면
        print("Korea")

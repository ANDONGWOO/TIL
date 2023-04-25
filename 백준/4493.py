import sys
sys.stdin = open("4493.txt", "r")

t=int(input())
for i in range(t):
    s=int(input())#가위 바위 보를 한 횟수
    #R바위 P보 S가위
    s1=0
    s2=0
    for j in range(s):
        a,b= map(str,input().split())
        if (a=="R" and b=="S")or(a=="P" and b=="R")or(a=="S" and b=="P"):#Player 1 승자이면 +1
            s1+=1
        elif (b=="R" and a=="S")or(b=="P" and a=="R")or(b=="S" and a=="P"):#Player 2 승자이면 +1
            s2+=1
    if s1>s2:
        print("Player 1")
    elif s1<s2:
        print("Player 2")
    else:
        print("TIE")

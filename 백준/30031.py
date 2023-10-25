import sys

sys.stdin = open("30031.txt", "r")
t=int(input())
s=0
for _  in range(t):
    a,b=map(int,input().split())
    if a==136:
        s+=1000
    elif a==142:
        s+=5000
    elif a==148:
        s+=10000
    else:
        s+=50000
print(s)
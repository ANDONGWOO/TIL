import sys
sys.stdin = open("27433.txt", "r")

t=int(input())
s=1
if t>0:
    for i in range(1,t+1):
        s *= i
print(s)
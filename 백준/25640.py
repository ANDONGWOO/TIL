import sys

sys.stdin = open("25640.txt", "r")

q=input()
t=int(input())
s=0#동일한 수
for i in range(1,t+1):
    w=input()
    if q==w:
        s+=1
print(s)
import sys
sys.stdin = open("7595.txt", "r")

a='*'
while 1:
    t=int(input())
    if t==0:
        break
    for i in range(1,t+1):
        print(a*i)
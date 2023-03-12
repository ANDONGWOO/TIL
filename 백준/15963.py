import sys
sys.stdin = open("15963.txt", "r")

a,b=map(int,input().split())

if a==b:
    print(1)
else:
    print(0)
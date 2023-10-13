import sys

sys.stdin = open("13597.txt", "r")

a,b=map(int,input().split())

if a>b:
    print(a)
else:
    print(b)
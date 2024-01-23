import sys

sys.stdin = open("25625.txt", "r")

a,b=map(int,input().split())

if a>b:
    print(a+b)
    sys.exit(0)
print(b-a)
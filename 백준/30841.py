import sys
sys.stdin = open("30841.txt", "r")


a,b = map(int, input().split())


if a>0 or b>0:
    print(int(a*b/(a+b)))
else:
    print(0)
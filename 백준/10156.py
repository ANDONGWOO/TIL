import sys

sys.stdin = open("10156.txt", "r")

a,b,c=map(int, input().split())


if a*b<=c:
    print(0)
if a*b>c:
    print((a*b)-c)
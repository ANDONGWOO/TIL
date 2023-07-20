import sys

sys.stdin = open("19698.txt", "r")

a,b,c,d=map(int,input().split())

if a<(b//d)*(c//d):
    print(a)
    sys.exit(0)
print((b//d)*(c//d))
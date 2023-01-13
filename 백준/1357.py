import sys

sys.stdin = open("1357.txt", "r")

a,b=map(str,input().split())

a,b=int(a[::-1]),int(b[::-1])

print(int(str(a+b)[::-1]))
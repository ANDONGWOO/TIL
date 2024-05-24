import sys
sys.stdin = open("31607.txt", "r")

a=int(input())
b=int(input())
c=int(input())

if a+b+c-max(a,b,c)==max(a,b,c):
    print(1)
else:
    print(0)
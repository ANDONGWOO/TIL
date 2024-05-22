import sys
sys.stdin = open("31654.txt", "r")

a,b,c=map(int,input().split())


if a+b==c:
    print("correct!")
else:
    print("wrong!")
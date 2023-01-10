import sys

sys.stdin = open("16430.txt", "r")

a,b=map(int,input().split())
print(b-a,b)
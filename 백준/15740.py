import sys

sys.stdin = open("15740.txt", "r")

A,B=map(int,input().split())
print(A+B)
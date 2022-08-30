import sys

sys.stdin = open("15964.txt", "r")

a,b=map(int,input().split())

print((a+b)*(a-b))
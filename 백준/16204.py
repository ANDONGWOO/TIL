import sys

sys.stdin = open("16204.txt", "r")

a,b,c=map(int,input().split())

print(min(b,c)+a-max(b,c))
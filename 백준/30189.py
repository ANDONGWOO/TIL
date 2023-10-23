import sys

sys.stdin = open("30189.txt", "r")


n,m=map(int,input().split())

print((n+1)*(m+1))
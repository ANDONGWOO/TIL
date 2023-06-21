import sys

sys.stdin = open("1434.txt", "r")


a,b=map(int,input().split())


q=list(map(int,input().split()))
w=list(map(int,input().split()))

print(sum(q)-sum(w))
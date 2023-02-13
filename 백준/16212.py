import sys

sys.stdin = open("16212.txt", "r")

n=int(input())

s=list(map(int,input().split()))
s.sort()
print(*s)
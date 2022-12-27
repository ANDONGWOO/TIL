import sys
sys.stdin = open("21964.txt", "r")

s=int(input())

q=list(input())
print(*q[-5:], sep="")
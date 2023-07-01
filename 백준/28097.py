import sys

sys.stdin = open("28097.txt", "r")


n=int(input())

q=list(map(int,input().split()))
w=sum(q)+8*(n-1)
print(w//24, w%24)


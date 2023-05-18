import sys

sys.stdin = open("14487.txt", "r")

n=int(input())

q=list(map(int,input().split()))
q.remove(max(q))
print(sum(q))
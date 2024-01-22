import sys
sys.stdin = open("31281.txt", "r")

q=list(map(int,input().split()))

q.sort()
print(q[1])
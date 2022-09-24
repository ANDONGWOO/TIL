import sys

sys.stdin = open("10823.txt", "r")
input=sys.stdin.readline



q=[i for i in input().split()]
w=[]
for i in q:
    w.append(i)
print(w)
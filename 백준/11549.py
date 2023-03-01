import sys

sys.stdin = open("11549.txt", "r")

q=input()
w=list(input())

print(w.count(q))
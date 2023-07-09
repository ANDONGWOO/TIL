import sys

sys.stdin = open("5789.txt", "r")

t=int(input())

for i in range(t):
    q=list(input())
    w=int(len(q)/2)
    if q[w]==q[w-1]:
        print("Do-it")
    else:
        print("Do-it-Not")
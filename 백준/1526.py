import sys

sys.stdin = open("1526.txt", "r")

q=int(input())

while 1:
    t=True
    for j in str(q):
        if j!="4" and j!="7":
            t = False
            q-=1
    if t:
        print(q)
        break
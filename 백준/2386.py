import sys

sys.stdin = open("2386.txt", "r")

while 1:
    q=input()
    if q=='#':
        break
    a=q[0]
    b=q[1:].lower()
    print(a,b.count(a))
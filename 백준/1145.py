import sys

sys.stdin = open("1145.txt", "r")

q=list(map(int, input().split()))

z=min(q)

while 1:
    w=0
    for i in q:
        if z%i==0:
            w+=1
    if w>2:
        break
    z+=1
print(z)

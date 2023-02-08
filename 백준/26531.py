import sys

sys.stdin = open("26531.txt", "r")

t=input().split()
q=int(t[0])
w=int(t[2])
e=int(t[4])

if q+w==e:
    print('YES')
else:
    print('NO')
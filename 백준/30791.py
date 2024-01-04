import sys
sys.stdin = open("30791.txt", "r")

a, b, c, d, e = map(int, input().split())
s = 0
if a - 1000 <= b:
    s += 1
if a - 1000 <= c:
    s += 1
if a - 1000 <= d:
    s += 1
if a - 1000 <= e:
    s += 1
print(s)
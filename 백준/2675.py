import sys

sys.stdin = open("2675.txt", "r")

t = int(input())
for i in range(t):
    q, s = input().split()
    a = ''
    for i in s:
        a += int(q) * i
    print(a)

import sys
sys.stdin = open("1075.txt", "r")

n = int(input())
f = int(input())

q = n // 100
w = q * 100

while w % f != 0:
    w += 1

print(str(w)[-2:])
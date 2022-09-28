import sys

sys.stdin = open("14489.txt", "r")

a, b = map(int, input().split())

c = int(input())

if a + b == (2 * c) or a + b > (2 * c):  # a+b가 2*c랑 동일하거나 크면
    print((a + b) - 2 * c)
else:
    print(a + b)

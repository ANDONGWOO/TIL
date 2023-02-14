import sys

sys.stdin = open("6438.txt", "r")

t=int(input())
for i in range(t):
    a=input()[::-1]
    print(a)
    
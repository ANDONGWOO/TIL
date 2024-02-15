import sys

sys.stdin = open("30045.txt", "r")

n=int(input())

s=0

for _ in range(n):
    q=input()

    if "01" in q or "OI" in q:
        s += 1
print(s)
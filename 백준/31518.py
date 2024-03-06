import sys
sys.stdin = open("31518.txt", "r")
n=int(input())
s=0
for _ in range(3):
    q=input().split()
    if '7' not in q:
        print(0)
        sys.exit(0)
print(777)

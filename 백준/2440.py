import sys

sys.stdin = open("2440.txt", "r")

s=int(input())

for i in range(s+1):
    print('*'*(s-i))
import sys

sys.stdin = open("2441.txt", "r")

s=int(input())

for i in range(s):
    print(((s-i)*'*').rjust(s))
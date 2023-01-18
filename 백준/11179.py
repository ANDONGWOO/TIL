import sys

sys.stdin = open("11179.txt", "r")
t=int(input())
a=str(bin(t)[2:])[::-1]

print(int(a,2))
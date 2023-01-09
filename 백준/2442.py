import sys

sys.stdin = open("2442.txt", "r")


s=int(input())

for i in range(1,s+1):
    print(" "*(s-i)+"*"*(2*i-1))
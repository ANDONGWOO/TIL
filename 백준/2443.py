import sys

sys.stdin = open("2443.txt", "r")


s=int(input())

for i in range(s,0,-1):
    print(" "*(s-i)+"*"*(2*i-1))
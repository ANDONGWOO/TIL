import sys

sys.stdin = open("1252.txt", "r")

t=list(map(str, input().split()))
s=int(t[0],2)+int(t[1],2)
print(bin(s)[2:])
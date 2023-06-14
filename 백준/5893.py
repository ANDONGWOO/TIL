import sys

sys.stdin = open("5893.txt", "r")

q=input()
print(bin(int(q,2)*17)[2:])
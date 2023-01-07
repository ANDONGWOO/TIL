import sys

sys.stdin = open("9659.txt", "r")

n = int(input())
if n%2 == 0:
    print("CY")
else:
    print("SK")
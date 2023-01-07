import sys

sys.stdin = open("9657.txt", "r")

n=int(input())
if n%7 == 2 or n%7 == 0:
    print("CY")
else:
    print("SK")

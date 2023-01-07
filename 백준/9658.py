import sys

sys.stdin = open("9658.txt", "r")

n = int(input())
if n%7 == 1 or n%7 == 3:
    print("CY")
else:
    print("SK")

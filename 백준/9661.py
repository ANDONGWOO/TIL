import sys

sys.stdin = open("9661.txt", "r")

n=int(input())
if n%5 == 2 or n%5 == 0:
    print("CY")
else:
    print("SK")
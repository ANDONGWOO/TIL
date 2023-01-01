import sys

sys.stdin = open("9656.txt", "r")

a=int(input())
if a%2==0:
    print("SK")
else:
    print("CY")
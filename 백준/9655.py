
import sys

sys.stdin = open("9655.txt", "r")

a=int(input())
if a%2==0:
    print("CY")
else:
    print("SK")
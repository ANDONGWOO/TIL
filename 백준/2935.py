
import sys

sys.stdin = open("2935.txt", "r")

a=int(input())
c=input()
b=int(input())
if c=='*':
    print(a*b)
else:
    print(a+b)
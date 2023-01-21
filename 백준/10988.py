import sys
sys.stdin = open("10988.txt", "r")

t=list(input())
if list(reversed(t)) == t:
    print(1)
else:
    print(0)
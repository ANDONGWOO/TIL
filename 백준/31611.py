import sys
sys.stdin = open("31611.txt", "r")

x=int(input())
if x%7==2:
    print(1)
else:
    print(0)
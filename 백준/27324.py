import sys

sys.stdin = open("27324.txt", "r")

a=list(input())

if a[0]==a[1]:
    print("1")
else:
    print("0")
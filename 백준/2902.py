import sys

sys.stdin = open("2902.txt", "r")


a=list(input().split('-'))

for i in a:
    print(i[0], end="")
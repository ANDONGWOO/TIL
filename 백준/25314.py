import sys

sys.stdin = open("25314.txt", "r")

s=int(input())

a=s//4

w=["long,"*a]
for i in w:
    print(*(i+"int").split(","))
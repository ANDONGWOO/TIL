import sys

sys.stdin = open("23803.txt", "r")

n=int(input())

for i in range(n*5):
    if i< 4*n:
        for i in range(n):
            print("@",end="")
    if i>= 4*n:
        for i in range(n*5):
            print("@",end="")
    print()
import sys

sys.stdin = open("23802.txt", "r")

n=int(input())

for i in range(n*5):
    if i<n:
        for i in range(n*5):
            print("@",end="")
    else:
        for i in range(n):
            print("@",end="")
    print()
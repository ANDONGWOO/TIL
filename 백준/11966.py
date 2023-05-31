import sys
sys.stdin = open("11966.txt", "r")

n=int(input())

for i in range(31):
    if 2**i == n :
        print(1)
        break
else:
    print(0)
        
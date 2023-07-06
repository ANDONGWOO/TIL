import sys

sys.stdin = open("1247.txt", "r")
for _ in range(3):
    n = int(sys.stdin.readline())
    q = [int(sys.stdin.readline()) for i in range(n)]
    if sum(q) < 0:
        print("-")
    elif sum(q) > 0:
        print("+")
    else:
        print("0")
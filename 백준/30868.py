import sys
sys.stdin = open("30868.txt", "r")

s=int(input())


for i in range(s):
    q=int(input())
    w1, w2 = divmod(q, 5)
    output = "++++ " * w1 + "|" * w2
    print(output)
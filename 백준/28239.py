import sys
import math
sys.stdin = open("28239.txt", "r")


t=int(input())

for i in range(t):
    q=int(input())
    w = int(math.log2(q))
    for i in range(w + 1):
        for j in range(i, w + 1):#0~w+1
            # 처음 2^0 2^0
            if 2**i + 2**j == q:
                print(i,j)

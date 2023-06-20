import sys
import math
sys.stdin = open("9076.txt", "r")


t=int(input())

for _ in range(t):
    q=list(map(int,input().split()))
    q.remove(max(q))#원래리스트에서 max
    q.remove(min(q))#원래리스트에서 min
    if max(q)<min(q)+4:
        print(sum(q))
    else:
        print("KIN")

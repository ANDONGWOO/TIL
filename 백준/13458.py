import sys
import math
sys.stdin = open("13458.txt", "r")

n=int(input())
a=list(map(int, input().split()))
b,c=map(int,input().split())
s=n
for i in a:
    if math.ceil((i-b)/c)>=1:
        s+=math.ceil((i-b)/c)
print(s)

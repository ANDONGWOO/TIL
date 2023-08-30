import sys
import math
sys.stdin = open("5347.txt", "r")

def lcm(a,b):#최소공배수
    return a*b/math.gcd(a,b)

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(int(lcm(a,b)))

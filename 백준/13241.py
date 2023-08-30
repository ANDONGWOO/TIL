import sys
import math
sys.stdin = open("13241.txt", "r")


def lcm(a,b):#최소공배수
    return a*b/math.gcd(a,b)
a,b=map(int,input().split())

print(int(lcm(a,b)))
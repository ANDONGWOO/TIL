import sys
import math
sys.stdin = open("1934.txt", "r")


def lcm(a, b):

    return a*b //math.gcd(a,b)


t=int(input())



for i in range(t):
    A,B=map(int, input().split())
    print(lcm(A,B))

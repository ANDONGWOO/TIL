
import sys
import math
sys.stdin = open("2869.txt", "r")
input=sys.stdin.readline
a,b,v=map(int,input().split())

q=(v - b) / (a - b)
print(math.ceil(q))

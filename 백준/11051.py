import sys
from math import factorial
sys.stdin = open("11051.txt", "r")

n, k = map(int, input().split())
b = factorial(n) // (factorial(k) * factorial(n - k))
print(b%10007)

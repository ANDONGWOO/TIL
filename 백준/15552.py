
import sys
sys.stdin = open("15552.txt", "r")

T=int(input())
for i in range(T):
        a,b=map(int, sys.stdin.readline().split())
        print(a+b)
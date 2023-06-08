import sys

sys.stdin = open("25191.txt", "r")

n=int(input())

a,b=map(int,input().split())

print(min(n,a//2+b))
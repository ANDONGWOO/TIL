import sys

sys.stdin = open("2420.txt", "r")
input=sys.stdin.readline
n,m=map(int, input().split())
q=n-m
print(abs(q))#절대값
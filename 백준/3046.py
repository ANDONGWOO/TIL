import sys
sys.stdin = open("3046.txt", "r")

a,b=map(int,input().split())

print(b*2-a)
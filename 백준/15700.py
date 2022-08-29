import sys
sys.stdin = open("15700.txt", "r")

a,b,=map(int,input().split())

c=a*b

print(c//2)

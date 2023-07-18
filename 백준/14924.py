import sys
sys.stdin = open("14924.txt", "r")

a,b,c=map(int,input().split())

q=c/(a*2)
print(int(q*b))
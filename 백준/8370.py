import sys
sys.stdin = open("8370.txt", "r")

a,b,c,d=map(int,input().split())

print((a*b)+(c*d))
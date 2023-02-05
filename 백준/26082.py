import sys

sys.stdin = open("26082.txt", "r")

a,b,c=map(int,input().split())

print(b//a*3*c)
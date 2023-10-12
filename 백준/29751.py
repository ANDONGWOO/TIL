import sys

sys.stdin = open("29751.txt", "r")


a,b=map(int,input().split())

print(float(a*b)/2)
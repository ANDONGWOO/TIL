import sys

sys.stdin = open("28444.txt", "r")

h,i,a,r,c=map(int,input().split())

print((h*i)-a*r*c)

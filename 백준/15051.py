import sys

sys.stdin = open("15051.txt", "r")

a=int(input())
b=int(input())
c=int(input())

print(min(b*2+c*4,a*2+c*2,a*4+b*2))

#1층,2층,3층설치순서
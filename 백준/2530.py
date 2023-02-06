import sys

sys.stdin = open("2530.txt", "r")

a,b,c=map(int,input().split())

t=int(input())

c+=t
b+=c//60
a+=b//60

print(a%24,b%60,c%60)
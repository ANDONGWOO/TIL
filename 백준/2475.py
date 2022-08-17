import sys


sys.stdin = open("2475.txt", "r")

a,b,c,d,f=map(int,input().split())

print((a**2+b**2+c**2+d**2+f**2)%10)
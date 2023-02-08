import sys
sys.stdin = open("18411.txt", "r")

a,b,c=map(int,input().split())

print((a+b+c)-min(a,b,c))
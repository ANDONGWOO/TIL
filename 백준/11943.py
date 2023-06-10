import sys
sys.stdin = open("11943.txt", "r")
a,b=map(int,input().split())
c,d=map(int,input().split())
print(min(a+d,c+b))
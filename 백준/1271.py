import sys

sys.stdin = open("1271.txt", "r")
a,b=map(int,input().split())
s=int(a//b)
q=a%b
print(s)
print(q)
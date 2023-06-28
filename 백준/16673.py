import sys

sys.stdin = open("16673.txt", "r")

c,k,p=map(int, input().split())

s=0
for i in range(c+1):
    s+=k*i + p*(i**2)
print(s)

import sys

sys.stdin = open("2748.txt", "r")

t=int(input())
a,b= 0,1

for i in range(t):
    a,b= b,a+b
print(a)
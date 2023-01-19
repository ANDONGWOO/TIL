import sys
sys.stdin = open("15624.txt", "r")

t=int(input())
a,b= 0,1

for i in range(t):
    a,b= b%1000000007,(a+b)%1000000007
print(a)
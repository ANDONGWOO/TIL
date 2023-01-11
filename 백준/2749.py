import sys

sys.stdin = open("2749.txt", "r")

t=int(input())
a,b= 0,1
for i in range(t%(15*1000000)):#1000 변화x
    a,b=b%1000000,(a+b)%1000000#문제 1000000
print(a)
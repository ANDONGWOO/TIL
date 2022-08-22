
import sys

sys.stdin = open("2525.txt", "r")

a,b=map(int, input().split())
c=int(input())

for i in range(c):
    b+=1
    if b==60:
        b=0
        a+=1
    if a==24:
        a=0
print(a,b)
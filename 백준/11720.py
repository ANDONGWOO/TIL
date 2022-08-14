
import sys
sys.stdin = open("11720.txt", "r")

n=int(input())
a=list(input())
b=0
for i in a:
    b+=int(i)
print(b)

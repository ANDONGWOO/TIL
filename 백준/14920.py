
import sys
sys.stdin = open("14920.txt", "r")
n=int(input())
s=1
while n!=1:
    if n%2:
        n=3*n+1
    else:
        n=n//2
    s+=1
print(s)

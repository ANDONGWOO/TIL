import sys

sys.stdin = open("10824.txt", "r")

a,b,c,d=input().split()
q=int(a+b)
w=int(c+d)

print(q+w)
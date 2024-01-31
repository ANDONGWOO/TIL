import sys

sys.stdin = open("31261.txt", "r")


a, b = map(int, input().split())
c=a+b
d=c*a
q=d+a
w=q*a
print(w)
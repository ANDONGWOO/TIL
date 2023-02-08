import sys

sys.stdin = open("15232.txt", "r")

a=int(input())
b=int(input())


for i in range(a):
    print('*'*b)
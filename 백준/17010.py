import sys
sys.stdin = open("17010.txt", "r")

t=int(input())

for i in range(t):
    a=input().split()
    print(int(a[0])*a[1])
import sys
sys.stdin = open("17256.txt", "r")

a=list(input().split())
b=list(input().split())

print(int(b[0])-int(a[2]),int(b[1])//int(a[1]),int(b[2])-int(a[0]))

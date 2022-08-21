import sys
sys.stdin = open("11004.txt", "r")

n,k=map(int, input().split())

a=list(map(int, input().split()))
a.sort()
print(a[k-1])


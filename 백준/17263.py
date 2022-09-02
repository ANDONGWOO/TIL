import sys
sys.stdin = open("17263.txt", "r")

n=int(input())
s=list(map(int,input().split()))
s.sort()
print(s[-1])
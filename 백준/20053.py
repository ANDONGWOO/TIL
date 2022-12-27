import sys
sys.stdin = open("20053.txt", "r")

t=int(input())

for i in range(1,t+1):
    q=int(input())# 정수 n개
    w=list(map(int, input().split()))
    print(min(w),max(w))

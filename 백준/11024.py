import sys

sys.stdin = open("11024.txt", "r")

T = int(input())

for i in range(1,T+1):
    N=list(map(int,input().split()))
    print(sum(N))
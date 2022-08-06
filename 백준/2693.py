from re import A, T
import sys
sys.stdin = open("2693.txt", "r")

T=int(input())

for z in range(1,T+1):
    A=list(map(int,input().split()))
    for i in A:
        A.sort()
    print(A[-3])
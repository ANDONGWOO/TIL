import sys
sys.stdin = open("3034.txt", "r")

n,w,h=map(int,input().split())

for i in range(n):
    s=(w**2+h**2)**0.5#a제곱+b제곱=c제곱
    r=int(input())
    if s>=r:
        print("DA")
    else:
        print("NE")
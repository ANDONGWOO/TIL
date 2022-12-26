import sys

sys.stdin = open("2075.txt", "r")
input = sys.stdin.readline
T=int(input())
a=[]

for i in range(1,T+1):
    a+=list(map(int,input().split()))
    a = sorted(a,reverse=True)[:T]
print(a[-1])

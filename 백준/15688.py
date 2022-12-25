import sys
sys.stdin = open("15688.txt", "r")
input= sys.stdin.readline


N=int(input())
a=[int(input()) for _ in range(N)]
a.sort()
for i in a:
    print(i)
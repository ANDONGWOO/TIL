
import sys
sys.stdin = open("11931.txt", "r")
input= sys.stdin.readline

N=int(input())
a=[int(input()) for _ in range(N)]
a.sort(reverse=True)
for i in a:
    print(i)
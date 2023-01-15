import sys
sys.stdin = open("5576.txt", "r")

w=sorted(int(input())for _ in range(10))[7:]
k=sorted(int(input())for _ in range(10))[7:]

print(sum(w),sum(k))
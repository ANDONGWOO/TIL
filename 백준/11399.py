import sys

sys.stdin = open("11399.txt", "r")

q=int(input())
w=list(map(int,input().split()))

w.sort()
s=0
for i in range(q):
    for j in range(i+1):
        s+=w[j]#1+3+6+9+13
print(s)
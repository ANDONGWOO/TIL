import sys

sys.stdin = open("14568.txt", "r")

n=int(input())
q=0
for i in range(2,n-1,2):
    q+=(n-i-2)//2
print(q)
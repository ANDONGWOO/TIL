import sys

sys.stdin = open("1912.txt", "r")


q=int(input())
w=list(map(int,input().split()))

for i in range(1,q):
    w[i]=max(w[i], w[i]+w[i-1])
print(max(w))

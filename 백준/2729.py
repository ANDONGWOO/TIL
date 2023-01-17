import sys

sys.stdin = open("2729.txt", "r")


q=int(input())
for i in range(q):
    t=list(map(str, input().split()))
    s=int(t[0],2)+int(t[1],2)
    print(bin(s)[2:])
import sys
sys.stdin = open("18795.txt", "r")

n,m=map(int, input().split())
s=0

for i in range(2):#n,m 2줄
    s+=sum(map(int, input().split()))
print(s)
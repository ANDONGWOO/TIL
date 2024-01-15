import sys
sys.stdin = open("30979.txt", "r")

t=int(input())
n=int(input())
f=list(map(int,input().split()))
if sum(f)>=t:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")
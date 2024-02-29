import sys
sys.stdin = open("31450.txt", "r")


a,b=map(int,input().split())
if a % b == 0:
    print("Yes")
else:
    print("No")



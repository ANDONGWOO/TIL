import sys
sys.stdin = open("10174.txt", "r")



t=int(input())
for i in range(t):
    s=input().lower()
    if s == s[::-1]:
        print("Yes")
    else:
        print("No")
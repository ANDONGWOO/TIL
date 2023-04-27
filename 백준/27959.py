import sys
sys.stdin = open("27959.txt", "r")

a,b=map(int,input().split())

if (a*100)>=b:
    print("Yes")
else:
    print("No")
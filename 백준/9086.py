import sys
sys.stdin = open("9086.txt", "r")

t=int(input())
for i in range(t):
    s=input()
    print(s[0]+s[-1])
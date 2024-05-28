import sys
sys.stdin = open("31616.txt", "r")


s=int(input())

q=set(input())

if len(q)==1:
    print("Yes")
else:
    print("No")
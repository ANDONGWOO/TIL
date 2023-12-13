import sys
sys.stdin = open("30501.txt", "r")

s=int(input())
for i in range(s):
    q=input()
    if q.count("S")>=1:
        print(q)
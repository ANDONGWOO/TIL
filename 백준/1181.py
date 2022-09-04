
import sys

sys.stdin = open("1181.txt", "r")
input=sys.stdin.readline

n=int(input())
w=[]
for i in range(n):
    s=input().strip()
    w.append(s)
w=list(set(w))
w.sort()
w.sort(key=len)
for i in w:
    print(i)

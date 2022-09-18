import sys

sys.stdin = open("25192.txt", "r")
input=sys.stdin.readline
n=int(input())
w=[]
for i in range(n):
    q=input().strip()
    w.append(q)
    e=set(w)
if 'ENTER'==e:
    len(e)
print(len(e)-1)
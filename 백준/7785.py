import sys
sys.stdin = open("7785.txt", "r")
input= sys.stdin.readline
t=int(input())
q=[]
w=[]
for _ in range(1,t+1):
    a,b=map(str,input().split())
    if b=="enter":
        q.append(a)
    else:
        q.remove(a)
q=sorted(q, reverse=True)
print(*q, sep="\n")
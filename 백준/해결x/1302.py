import sys

sys.stdin = open("1302.txt", "r")

t=int(input())
a=[]
w=[]
q=[]
for i in range(1,t+1):
    a+=input().split()
for j in a:
    w.append(a.count(j))
    if a.count(j)==max(w):    
        q.append(j)
q.sort()
print(q[0])

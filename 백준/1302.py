import sys

sys.stdin = open("1302.txt", "r")

t=int(input())
a=[]
q={}
for i in range(t):
    a=input()
    if a not in q:
        q[a]=1
    else:
        q[a]+=1
w=[]
z=max(q.values())
for i in q:
    if z==q[i]:
        w.append(i)
w.sort()
print(w[0])
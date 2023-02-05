import sys

sys.stdin = open("1120.txt", "r")

a,b=map(str, input().split())

q=[]
for i in range(len(b)-len(a)+1):
    w=0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            w+=1
    q.append(w)
print(min(q))
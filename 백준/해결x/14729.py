import sys

sys.stdin = open("14729.txt", "r")

T=int(input())
b=[]
c=[]
for i in range(1,T+1):
    b.append(input())
    c=sorted(b,key=lambda x: x[0])
c.remove(c[-1])
print(*c,sep="\n")

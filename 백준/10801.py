import sys

sys.stdin = open("10801.txt", "r")

a=list(map(int,input().split()))
b=list(map(int,input().split()))

q=0#a승수
w=0#b승수
for i in range(10):
    if a[i]>b[i]:
        q+=1
    if a[i]<b[i]:
        w+=1
    else:
        q+=0
        w+=0
if q==w:
    print("D")
if q>w:
    print("A")
if q<w:
    print("B")
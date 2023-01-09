import sys
sys.stdin = open("22966.txt", "r")
t=int(input())
b=[]
for i in range(t):
    a=input().split()
    b.append(a)
b=sorted(b,key=lambda x:x[1])
print(b[0][0])
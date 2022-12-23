import sys

sys.stdin = open("1822.txt", "r")

A=map(int,input().split())

a=set(map(int,input().split()))#변화x
b=set(map(int,input().split()))#변화x
s=[]
for i in a:
    if i not in b:#b에 i가없다
        s.append(i)#s에 추가
       
s.sort()
if len(s)==0:
    print(0)
else:
    print(len(s))
    print(*s)
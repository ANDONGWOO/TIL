import sys
sys.stdin = open("18408.txt", "r")

a,b,c=map(int,input().split())
s1=0
s2=0
if a==1:
    s1+=1
else:
    s2+=1
if b==1:
    s1+=1
else:
    s2+=1
if c==1:
    s1+=1
else:
    s2+=1
if s1>s2:
    print(1)
else:
    print(2)

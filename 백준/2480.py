import sys

sys.stdin = open("2480.txt", "r")

a,b,c=map(int,input().split())
s=0
if a==b==c:
    s=10000+(a*1000)
elif a==b or a==c:
    s=1000+(a*100)
elif b==c:
    s=1000+(b*100)
elif a!=b!=c:
    s=max(a,b,c)*100
print(s)
 
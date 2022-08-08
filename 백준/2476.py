import sys

sys.stdin = open("2476.txt", "r")

N=int(input())
s=[]
for z in range(N):
    a,b,c=map(int,input().split())
    if a==b==c:
        s.append(10000+(a*1000))
    elif a==b:
        s.append(1000+(a*100))
    elif a==c:
        s.append(1000+(a*100))    
    elif b==c:
        s.append(1000+(b*100))
    else:
        s.append(max(a,b,c)*100)
print(max(s))
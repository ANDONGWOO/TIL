import sys

sys.stdin = open("25628.txt", "r")
a,b =map(int,input().split())
s=0
while True:
    if a>=2 and b>=1:
        a-=2
        b-=1
        s+=1
    else:
        print(s)
        break
    

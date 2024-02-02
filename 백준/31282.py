import sys
sys.stdin = open("31282.txt", "r")
a,b,c=map(int,input().split())
s=0
while 1 :
    if a<=0:
        break
    a+=b
    a-=c
    s+=1
print(s)
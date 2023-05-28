import sys
sys.stdin = open("5532.txt", "r")

l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
s=0
while True:
    if a<=c*s and b<=d*s:
        break
    else:
        s+=1
        l-=1
print(l)

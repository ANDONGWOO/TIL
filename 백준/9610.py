from re import T
import sys

sys.stdin = open("9610.txt", "r")
N=int(input())

a=0
b=0
c=0
d=0
f=0 
for i  in range(N):
    x,y=map(int,input().split())
    if x>0 and y>0:
        a+=1        
    if x<0 and y>0:
        b+=1      
    if x<0 and y<0:
        c+=1
    if x>0 and y<0:
        d+=1      
    if y==0 or x==0:
        f+=1
print('Q1:',a)
print('Q2:',b)
print('Q3:',c)
print('Q4:',d)
print('AXIS:',f)
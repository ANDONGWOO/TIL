import sys

sys.stdin = open("10093.txt", "r")

a,b=map(int,input().split())
c=max(a,b)-min(a,b)-1
if max(a,b)==min(a,b) or min(a,b)+1==max(a,b):
    c=0
print(c)
for i in range(min(a,b)+1,max(a,b)):
   print(i,end=" ")
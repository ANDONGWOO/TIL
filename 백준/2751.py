from re import T
import sys

sys.stdin = open("2751.txt", "r")

N=int(input())
a=[]
for k in range(1,N+1):
    a.append(int(input()))
a=sorted(a) #위치에 따라 
for i in range(len(a)):
    print(a[i])
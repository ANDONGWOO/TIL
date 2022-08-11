from re import T
import sys
from tkinter import N

sys.stdin = open("1978.txt", "r")
T=int(input())
N=map(int,input().split())
q=0
for z in N:
    a=0
    if z>1:
        for i in range(2,z):
            if z%i ==0:
                a+=1
        if a==0:
            q+=1
print(q)
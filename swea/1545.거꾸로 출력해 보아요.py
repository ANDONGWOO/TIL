from re import T
import sys
from tkinter import N

sys.stdin = open("1545.txt", "r")


N=int(input())
a=[]
for i in range(N+1):#레인저 1~8
    if N-i!=0 or N-i==0:
        a=N-i
        print(a,end=' ')
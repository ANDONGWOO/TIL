
import sys
from tkinter import N
sys.stdin = open("9085.txt", "r")

T=int(input())
s=[]
for i in range(T):
    N=int(input())
    s=sum(list(map(int,input().split())))
    print(s)

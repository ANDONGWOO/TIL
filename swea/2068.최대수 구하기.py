
from re import T
import sys
from tkinter import N
sys.stdin = open("2068.txt", "r")

T=int(input())


for k in range(1,T+1):
    N=map(int,input().split())
    a=[]
    for i in N:
        a=max(N)
    print(f'#{k} {a}')

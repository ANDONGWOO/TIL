
from re import X
import sys
from tkinter import N
sys.stdin = open("10807.txt", "r")
while True:
    try:
        N=int(input())
        for q in range(1,N+1):
            s=0
            Z=list(map(int,input().split()))
            V=int(input())
            for i in Z:           
                Z.count(V)
            print(Z.count(V))
    except EOFError:
        break
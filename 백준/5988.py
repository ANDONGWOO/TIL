import sys
from tkinter import N

sys.stdin = open("5988.txt", "r")

n=int(input())
for i in range(n):
    k=int(input())
    if k%2==1:
        print('odd')
    else:
        print('even')


import sys
from tkinter import N
sys.stdin = open("2562.txt", "r")



a=[]
for i in range(9):
    n=int(input())
    a.append(n)
print(max(a))
print(a.index(max(a))+1)

from os import popen
import sys
from tkinter import E

sys.stdin = open("10817.txt", "r")

A=map(int,input().split())
b=sorted(A)
print(b[1])
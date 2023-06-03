import sys

sys.stdin = open("14624.txt", "r")

q=int(input())
if q%2==0:
    print("I LOVE CBNU")
else:
    print("*"*q)
    print(" "*((q//2)-1),"*")
    for i in range(q//2):
        print(" "*((q//2)-1-i)+ "*" + " " * (1+i*2) + "*")
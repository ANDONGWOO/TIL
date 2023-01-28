import sys
sys.stdin = open("15727.txt", "r")

t=int(input())

if t%5:
    print(t//5+1)
else:
    print(t//5+0)
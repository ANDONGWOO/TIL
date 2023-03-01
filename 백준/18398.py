import sys
sys.stdin = open("18398.txt", "r")

t1=int(input())

for i in range(t1):
    t2=int(input())
    for i in range(t2):
        a,b=map(int,input().split())
        print(a+b,a*b)
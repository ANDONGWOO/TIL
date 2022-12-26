import sys
sys.stdin = open("2711.txt", "r")

t=int(input())

for _ in range(1,t+1):
    a,b=input().split()
    b=list(b)
    a=int(a)
    b.pop(a-1)
    print(*b, sep="") 

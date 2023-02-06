import sys
sys.stdin = open("11815.txt", "r")

q=int(input())
w=list(map(int,input().split()))

for i in range(q):
    if w[i] == int(w[i]**0.5)**2:
        print(1,end=" ")
    else:
        print(0,end=" ")
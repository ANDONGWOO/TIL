import sys
sys.stdin = open("10188.txt", "r")

a=int(input())
for _ in range(a):
    q,w=map(int,input().split())
    for i in range(w):
        print(q*'X')
    print()
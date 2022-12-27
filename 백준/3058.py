import sys
sys.stdin = open("3058.txt", "r")
input= sys.stdin.readline
t=int(input())
for i in range(1,t+1):
    w=[]
    q=list(map(int, input().split()))
    for j in q:
        if j%2==0:
            w.append(j)
    
    print(sum(w),min(w))
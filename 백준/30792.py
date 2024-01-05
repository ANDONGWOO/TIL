import sys
sys.stdin = open("30792.txt", "r")

n=int(input())
a=list(map(int,input().split()))

w=list(map(int,input().split()))
e=a+w
e=sorted(e)


for i in e:
    if a[0]==i:
        print(n-e.index(i))
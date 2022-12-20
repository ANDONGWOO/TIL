import sys

sys.stdin = open("1920.txt", "r")

t1=int(input())
s1=set(map(int,input().split()))#시간을 줄이기 위해 set

t2=int(input())
s2=list(map(int,input().split()))
for i in s2:
    if i in s1:
        print(1)
    else:
        print(0)

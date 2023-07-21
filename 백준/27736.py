import sys

sys.stdin = open("27736.txt", "r")

n=int(input())
q=list(map(int,input().split())) 
if isinstance(n/2,int):#정수인지 확인
    if n/2<q.count(0):
        print("INVALID")
        sys.exit(0)
else:
    if n/2<=q.count(0):
        print("INVALID")
        sys.exit(0)
if q.count(1)>q.count(-1):
    print('APPROVED')
else:
    print("REJECTED")
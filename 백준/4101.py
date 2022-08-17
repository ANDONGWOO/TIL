import sys

sys.stdin = open("4101.txt", "r")

while 1:
    a,b=map(int,input().split())
    if a==0 and a==b:# 먼저 브레이크 설정
            break
    if a>b:
        print('Yes')
    else:
        print('No')
        
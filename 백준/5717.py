import sys

sys.stdin = open("5717.txt", "r")

while 1:
    try:
        for i in range(1,5+1):
            a,b=map(int,input().split())
            if a!=0 and b!=0:
                print(a+b)
            if a==0 and b==0:
                break
    except:
        break 

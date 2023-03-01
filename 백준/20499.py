import sys
sys.stdin = open("20499.txt", "r")

k,d,a=map(int,input().split("/"))
if k+a<d or d==0:
    print('hasu')
else:
    print('gosu')

import sys
import datetime
sys.stdin = open("1308.txt", "r")

a=list(map(int, input().split()))
b=list(map(int, input().split()))

q= datetime.date(a[0],a[1],a[2])#년,월,일
e= datetime.date(a[0]+1000, a[1],a[2])
w= datetime.date(b[0],b[1],b[2])#년,월,일

j=e-q
k=w-q

if k < j:
    print("D-{}".format(k.days))
else:
    print('gg')

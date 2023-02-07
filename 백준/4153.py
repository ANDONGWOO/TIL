import sys
sys.stdin = open("4153.txt", "r")

while 1:
    a=list(map(int,input().split()))
    if sum(a)==0:
        break
    a.sort()
    if a[0]**2 + a[1]**2 == a[2]**2:
        print('right')
    else:
        print('wrong')
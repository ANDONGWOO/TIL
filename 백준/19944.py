import sys
sys.stdin = open("19944.txt", "r")

n,m=map(int,input().split())

if m==1 or m==2:#m이  1이나2면
    print('NEWBIE!')
elif m<=n and (m!=1 and m!=2):#n이하면서 m이 1이나2가 아니면
    print('OLDBIE!')
else:#뉴비도 아니고 올드비아니면
    print('TLE!') 
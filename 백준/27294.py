import sys

sys.stdin = open("27294.txt", "r")

a,b= map(int,input().split())

if b==0 and(a>=12 and a<=16):#b==0 술x and a가 12이상 16이하면 점심
    print('320')
else:
    print('280')

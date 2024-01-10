import sys
sys.stdin = open("13866.txt", "r")

a,b,c,d=map(int,input().split())
print(abs((a+d)-(b+c)))
import sys
sys.stdin = open("7891.txt", "r")

t=int(input())#테스트 케이스 수수

for i in range(t):
    a,b=map(int,input().split())
    print(a+b)#a,b합
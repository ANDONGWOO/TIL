import sys

sys.stdin = open("2163.txt", "r")

n,m=map(int,input().split())
s=n*m#초콜릿의 조각수
q=0#초콜릿 1조각씩 만들기
while 1:
    if s!=1:
        s-=1#1조각 빼고
        q+=1#1조각 빼고 카운터
    if s==1:#s가 1조각 이면
        print(q)
        break

import sys

sys.stdin = open("1350.txt", "r")

n=int(input())
f=list(map(int,input().split()))
c=int(input())
s=0
for i in f:
    if i%c==0:#0
        s+=i//c#0
        #파일의 크기가 0같다면 클러스터 필요가 없다
    else:
        s+=i//c+1
        #파일의 크기가 0이아니면+1
        #몫 소수점이면 +1
        #몫 정수이면(1이상)i//c 실제 2 예1)600 512
        #클러스터 크기가 파일의 크기 보다 작다면 추가
print(s*c)
#파일의 크기가 0같다면 클러스터 필요가 없다
#클러스터 크기가 파일의 크기 보다 작다면 추가



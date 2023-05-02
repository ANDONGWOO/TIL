import sys
sys.stdin = open("27885.txt", "r")

c,h=map(int,input().split())
z=[]
for _ in range(c+h):
    q,w,e=map(int,input().split(":"))
    z.append(q*60*60+w*60+e)
z.sort()#먼저 접근한 순서
x=-40#통과 시간
s=0#총 통과시간(내려간 시간)
for i in z:
    #시간이 겹치는 확인
    if i-x>=40:#40이상 이면
        p=40
    else:#40보다 작다면
        p=i-x
    s+=p
    x=i
print(86400-s)
#24시간 초로 변산 86400 
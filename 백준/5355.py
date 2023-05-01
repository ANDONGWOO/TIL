import sys
sys.stdin = open("5355.txt", "r")

t=int(input())
s=0.0
for _ in range(t):#t 반복 
    q=list(map(str,input().split()))#테스트 케이스 리스트 받아서 len만큼 반복하고 
    s=float(q[0])
    for i in range(1,len(q)):
        if q[i]=="@":
            s*=3
        elif q[i] =="%":
            s+=5
        elif q[i] =="#":
            s-=7
    print("%0.2f"%s)#계산하고 값출력




#출력 값 소수점 2번째 까지
#t 반복 
# 테스트 케이스 리스트 받아서 len만큼 반복하고 
# 계산하고 값출력
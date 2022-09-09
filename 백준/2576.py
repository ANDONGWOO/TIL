import sys
sys.stdin = open("2576.txt", "r")
input=sys.stdin.readline

w=[]
s=0
e=[]
for i in range(7):#입력 값7
    q=int(input())
    w.append(q)#w에 q 하나씩 추가
    if w[i]%2==0:#7개중 전부짝수면-1출력 
        s+=1
        if s==7:#s가 7이면 -1출력
            print(-1)
            break
    elif w[i]%2==1:#홀수 리스트 만들고
        e.append(w[i])
else:
    print(sum(e))#e리스트(홀수합)합
    print(min(e))#e리스트 최소



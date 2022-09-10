import sys

sys.stdin = open("2953.txt", "r")
input=sys.stdin.readline
w=[]
for i in range(5):#참가자 수
    a,b,c,d=map(int,input().split())#점수
    w.append(a+b+c+d)#점수의 합 w에 추가 총점수 리스트
print(w.index(max(w))+1)#인덱스는 0부터 시작+1
print(max(w))#W최고 값

    
import sys

sys.stdin = open("1236.txt", "r")
input=sys.stdin.readline

n,m=map(int,input().split())

q=0
for i in range(n):#n세로
    s=list(input().strip())#공백문자 제거
    if "X" not in s:
        q+=1#s리스트 x 없다면 q에 1증가
print(q)
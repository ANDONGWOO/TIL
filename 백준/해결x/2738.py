import sys

sys.stdin = open("2738.txt", "r")
input=sys.stdin.readline
n,m=map(int,input().split())
w=[]
e=[]
z=[[],[],[]]
for i in range(n):#위3줄 
    a=list(map(int,input().split()))
    w.append(a)#a를 w추가 입력값 한줄씩 인덱스로 만들고
for i in range(n):
    b=list(map(int,input().split()))
    e.append(b)
    print(e[0])
 
import sys

sys.stdin = open("11047.txt", "r")

a,b = map(int, input().split())
q=[]#동전의 종류
s=0#매수
for i in range(1,a+1):
    q.append(int(input()))
q.sort(reverse=True)#50000부터 
for i in q:
    s+= b//i
    b%=i
print(s)

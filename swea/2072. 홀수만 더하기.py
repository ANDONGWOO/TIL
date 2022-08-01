
import sys
sys.stdin = open("2072.txt", "r")

T=int(input())

for k in range(1,T+1):
    N=map(int,input().split())
    a=0#위치가 변경되면 값이 변경
    for i in N:
        if i%2==1:
            a+=i
    print(f'#{k} {a}')#위치가 변경되면 값이 변경
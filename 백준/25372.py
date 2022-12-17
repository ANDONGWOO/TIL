import sys

sys.stdin = open("25372.txt", "r")

T=int(input())#테스트 케이스 수

for i in range(1,T+1):
    a=input()#테스트 케이스
    if 6 <= len(a) and len(a) <=9:#6이상 9이하
        print('yes')
    else:
        print("no")

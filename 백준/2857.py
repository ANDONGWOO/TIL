from re import T
import sys

sys.stdin = open("2857.txt", "r")

a=[]# 입력 리스트
for _ in range(5):
    a.append(input())
b=0
for i in range(len(a)):
    if 'FBI'in a[i]:
        print(i+1,end=' ')#인덱스+1 줄수 
        b=1
if b==0:
    print('HE GOT AWAY!')

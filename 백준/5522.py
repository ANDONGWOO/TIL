import sys
sys.stdin = open("5522.txt", "r")
input=sys.stdin.readline

q=0#총합
for i in range(5):#경기수
    s=int(input())#점수입력
    q+=s
print(q)



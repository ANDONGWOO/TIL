import sys

sys.stdin = open("2839.txt", "r")

s=int(input())
q=0
while s>=0:
    if s%5 ==0:#5배수일때
        q+=s//5
        print(q)
        break
    s-=3#5배수 아닐때 3kg담음
    q+=1
else:
    print(-1)
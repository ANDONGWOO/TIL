
import sys

sys.stdin = open("1110.txt", "r")


n=int(input())#n의 범수 0~99 10보다 작다면 앞0붙여 두자리수 만들고 그래서 n 두자리수
a=n
s=0

while True:
    q= a//10
    w= a%10
    e= (q+w)%10
    a=(w*10)+e
    s+=1
    if a==n:
        break
print(s)
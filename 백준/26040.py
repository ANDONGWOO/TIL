import sys

sys.stdin = open("26040.txt", "r")

a=list(input())
b=list(input().split())

for i in range(len(a)):
    for k in range(len(b)):
        if a[i]==b[k]:#요소 있다면
            a[i] = a[i].lower()#소문자로 변환
print(*a,sep="")
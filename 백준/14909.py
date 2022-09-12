import sys
sys.stdin = open("14909.txt", "r")

s=list(map(int,input().split()))
q=0
for i in range(len(s)):#s인덱스
    if s[i]>0:#0보다 크다면 1증가
        q+=1
print(q)
import sys
sys.stdin = open("11656.txt", "r")

s=list(input())
q=[]
for i in s:
    q.append(s)#처음 원래 s
    s=s[1:]#그다음부터 인덱스 0 빼면서
q.sort()
for i in q:
    print(*i,sep="")

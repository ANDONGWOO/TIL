import sys
sys.stdin = open("10815.txt", "r")
q=[]
t1=int(input())
s1=set(map(int,input().split()))#시간을 줄이기 위해 set

t2=int(input())
s2=list(map(int,input().split()))
for i in s2:
    if i in s1:
        q.append(1)
    else:
        q.append(0)
print(*q)
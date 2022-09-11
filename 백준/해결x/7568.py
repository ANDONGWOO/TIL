import statistics
import sys
sys.stdin = open("7568.txt", "r")

s=int(input())#전체 사람의수
w=[]
e=[]
for i in range(s):
    a,b=map(int,input().split())
    c=round((a+b)/2)#반올림하고 c할당
    c=round(c,-1)#십자리 까지 반올림
    w.append(c)
for j in w:
    if j==max(w):#j가 w최고값이랑동일하다면
        e=1
    elif j==statistics.median(w):#j가 w중간값이랑동일하다면
        e=2
    elif j==min(w):#j가 w최소값이랑동일하다면
        e=5
    print(e,end=" ")





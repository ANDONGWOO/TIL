
import sys

sys.stdin = open("2495.txt", "r")

for _ in range(3):
    q=list(input())
    s=1
    w=0
    for i in range(1,len(q)):
        if q[i]==q[i-1]:
            s+=1
            #실행하면 w=s
            #현재 s의 값
        else:
            #실행하면 w=1
            w=max(s,w)
            s=1
    w=max(s,w)
    print(w)
#기본값은 1(s)
#현재 인덱스에서 인덱스-1 같다면 s+1
#아니면 w리스트에 추가 s그리고 s=1 
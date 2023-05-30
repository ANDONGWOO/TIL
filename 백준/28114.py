import sys
sys.stdin = open("28114.txt", "r")

q=[[],[],[]]
w=[]
for i in range(3):
    a,b,c=map(str,input().split())
    q[i]=a,c
    w.append(str(int(b)%100))#다른리스트 저장
w.sort()
q.sort(reverse=True,key=lambda x:int(x[0]))#q 리스트 0인덱스 int기준 정렬
print(*w,sep="")
print(list(q[0][1])[0],list(q[1][1])[0],list(q[2][1])[0],sep="")#성씨 첫번째 글자

#lambda
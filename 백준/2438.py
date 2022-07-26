#별 하나씩 증가
N=int(input())

star1="*"
k=1
for i in  range(1,N+1):
    if i==k:
        i=star1
        star1+="*"
        k+=1
    print(i)
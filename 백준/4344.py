import sys
sys.stdin = open("4344.txt", "r")
c=int(input())
for i in range(c):
    a=list(map(int,input().split()))
    s=0
    q=0
    b=(sum(a[1::])/a[0])
    for i in a[1::]:
        if i>b :
            s+=1
    
    print(format((s/a[0])*100,".3f")+'%')


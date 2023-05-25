import sys

sys.stdin = open("2467.txt", "r")

n=int(input())

q=list(map(int,input().split()))
a,b=0,n-1#정렬순서
e=2000000000
while a<b:
    w=q[a]+q[b]
    # print("!@")
    if abs(w)<e:#abs 절대값/기본값
        A=a 
        B=b
        e=abs(w)
        # print(0)
        # print(A,B)
     
    if w>0:
        b-=1
        # print(b,"@")
    elif w<0:
        a+=1
        # print(a,"#")
    else:
        break
print(q[A],q[B])  

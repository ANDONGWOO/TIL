import sys
sys.stdin = open("2470.txt", "r")

n=int(input())

q=list(map(int,input().split()))
q.sort()
a,b=0,n-1
e=2000000000
while a<b:
    w=q[a]+q[b]

    if abs(w)<e:
        A=a 
        B=b
        e=abs(w)
    if w>0:
        b-=1

    elif w<0:
        a+=1
    else:
        break
print(q[A],q[B])
import sys
sys.stdin = open("2473.txt", "r")

n=int(input())

q=list(map(int,input().split()))
q.sort()
e=3000000000
z=[]
for i in range(n-2):
    a=i+1
    c=i
    b=n-1
    while a<b:
        w=q[a]+q[c]+q[b]
        if abs(w)<e:
            e=abs(w)
            z=[q[a], q[c], q[b]]
        if w>0:
            b-=1

        elif w<0:
            a+=1
        else:
            break
print(z[1],z[0],z[2])

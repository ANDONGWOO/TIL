import sys
sys.stdin = open("8932.txt", "r")

t=int(input())
a=[	9.23076,1.84523,56.0211,4.99087,0.188807,15.9803,0.11193]
b=[26.7,75,1.5,42.5,210,3.8,254]
c=[1.835,1.348,1.05,1.81,1.41,1.04,1.88]
for i in range(t):
    s=0
    p=list(map(int,input().split()))
    for i in range(7):
        if i==0 or i==3 or i==6:
            s+=int(a[i]*(b[i]-p[i])**c[i])
        else:
            s+=int(a[i]*(p[i]-b[i])**c[i])
    print(s)

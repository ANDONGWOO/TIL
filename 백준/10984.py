import sys
sys.stdin = open("10984.txt", "r")

T=int(input())
for i in range(T):
    t=int(input())
    s1=0
    s2=0
    for i in range(t):
        a,b=map(float,input().split())
        s1+=a
        s2+=b*a
    print(int(s1),round(s2/s1,1))
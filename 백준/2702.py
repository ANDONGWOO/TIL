import sys
sys.stdin = open("2702.txt", "r")

def lcm(a,b):#최소공배수
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            return i
        
def gcd(a,b):#최대공약수
    while b>0:
        a,b=b,a%b
    return a

t=int(input())

for _ in range(t):
    a,b=map(int,input().split())
    print(lcm(a,b),gcd(a,b))


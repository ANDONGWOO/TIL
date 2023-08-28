import sys

sys.stdin = open("28701.txt", "r")

n=int(input())
s1=0
s2=0
s3=0
for i in range(1,n+1):
    s1+=i
    s2+=i
    s3+=i**3
print(s1,s2**2,s3,sep="\n")
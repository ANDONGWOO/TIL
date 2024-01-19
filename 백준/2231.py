import sys
sys.stdin = open("2231.txt", "r")

n=int(input())


for i in range(1,n+1):
    s=sum(map(int,str(i)))
    n_s=i+s
    if n_s==n:
        print(i)
        sys.exit()
print(0)
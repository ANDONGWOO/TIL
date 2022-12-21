import sys

sys.stdin = open("1929.txt", "r")
a,b=map(int,input().split())

for i in range(a, b+1):
    if i == 1:#1이면 소수x
        continue
    for j in range(2, int(i** 0.5)+1 ):#제곱근
        if i%j==0:
            break
    else:
        print(i)
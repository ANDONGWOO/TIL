
#import sys

#sys.stdin = open("1933.txt", "r")

# 1부터 N길이 구하고
a = []
N = int(input())
# N까지 길이에서 약수 구하고
for i in (range(1,N+1)):
    
    if N % i == 0:
        a.append(i)
        a.sort()
for z in a:
    print(z ,end=" ")

# 정렬 하고 

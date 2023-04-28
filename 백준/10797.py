import sys

sys.stdin = open("10797.txt", "r")

q=int(input())
w=list(map(int,input().split()))
s=0
for i in range(5):
    if q == w[i]:
        s+=1
print(s)
#q가 w요소와 같다 +1
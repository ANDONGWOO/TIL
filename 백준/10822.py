import sys

sys.stdin = open("10822.txt", "r")

s=input().split(',')
q=0
for i in s:#s요소 i int변환하고 q에 증가
    q+=int(i)
print(q)
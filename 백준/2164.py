import sys
from collections import deque
sys.stdin = open("2164.txt", "r")

n=int(input())

a=deque(range(1,n+1))
while len(a)>1:
    a.popleft()
    a.append(a.popleft())
print(a[0])
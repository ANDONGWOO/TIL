from inspect import stack
import sys
sys.stdin = open("3986.txt", "r")
t=int(input())
s=0

for i in range(t):
    a=input().rstrip()
    stack=[]
    for j in range(len(a)):
        if stack and a[j] == stack[-1]:
            stack.pop()
        else:
            stack.append(a[j])
    if not stack:
        s+= 1
print(s)

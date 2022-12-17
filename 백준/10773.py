import sys

sys.stdin = open("10773.txt", "r")

stack=[]

T=int(input())

for i in range(1,T+1):
    s=int(input())
    if s !=0:
        stack.append(s)
    if s == 0:
        stack.pop()#pop기본 마지막/인자에 인덱스 넣어서 pop
print(sum(stack))
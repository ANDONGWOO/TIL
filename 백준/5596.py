import sys
sys.stdin = open("5596.txt", "r")

q=list(map(int,input().split()))
w=list(map(int,input().split()))
if sum(q)<sum(w):#q합 w합
    print(sum(w))#w크다면
else:
    print(sum(q))#q크다면

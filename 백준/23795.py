import sys

sys.stdin = open("23795.txt", "r")
q=0#총합 
while 1:
    s=int(input())
    if s==-1:#-1이 나오면 마지막이라 break
        break
    else:
        q+=s
print(q)
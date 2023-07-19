import sys

sys.stdin = open("28248.txt", "r")


a=int(input())
b=int(input())
s=a*50-b*10
if a<=b:
    pass
else:
    s+=500
print(s)
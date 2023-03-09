import sys

sys.stdin = open("1436.txt", "r")

q=int(input())
w=666
s=0
while 1:
    if "666" in str(w):
        s+=1
    if s==q:
        print(w)
        break
    w+=1
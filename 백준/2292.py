import sys
sys.stdin = open("2292.txt", "r")

n=int(input())

n_s=1#6씩증가 
s=1
while 1:
    if not n>n_s:
        break
    n_s+=6*s
    s+=1
print(s)
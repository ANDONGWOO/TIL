import sys

sys.stdin = open("1904.txt", "r")

q=int(input())
w,e=1,1
for i in range(q):
    w,e = e%15746 ,(w+e)%15746
print(w)
import sys
sys.stdin = open("8394.txt", "r")

q=int(input())
w,e = 1,0
for i in range(q):
    w,e = (w+e)%10, w%10
print(w)
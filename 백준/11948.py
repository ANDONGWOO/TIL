import sys
sys.stdin = open("11948.txt", "r")

q=[]

for _ in range(6):
    q.append(int(input()))
a=sorted(q[:4])
b=max(q[4:])
print(sum(a[1:])+b)
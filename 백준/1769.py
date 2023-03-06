import sys

sys.stdin = open("1769.txt", "r")

q=list(map(int, input().strip()))

s=0
while len(q) > 1:
    s+=1
    w=[]
    q=sum(q)
    for i in str(q):
        w.append(int(i))
    q=w
print(s)

if q[0]%3 == 0:
    print("YES")
else:
    print("NO")
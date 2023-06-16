import sys

sys.stdin = open("6840.txt", "r")

q=[]
for i in range(3):
    q.append(int(input()))
    q.sort()
print(q[1])
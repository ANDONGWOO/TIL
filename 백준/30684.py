import sys
sys.stdin = open("30684.txt", "r")

n=int(input())
q=[]

for i in range(n):
    w=input()
    if len(w)==3:
        q.append(w)
q.sort()
print(q[0])
import sys

sys.stdin = open("2789.txt", "r")

q=list(input())
w=['C','A','M','B','R','I','D','G','E']
e=[]
for i in q:
    if i not in w:
        e.append(i)
print(*e, sep="")

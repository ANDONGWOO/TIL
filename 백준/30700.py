import sys
sys.stdin = open("30700.txt", "r")

q=input()
w=0
s=0
e=['K', 'O', 'R', 'E', 'A']
for i in q:
    if e[w]==i:
        w+=1
        s+=1
    if w==5:
        w=0
print(s)
        
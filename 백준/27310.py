import sys

sys.stdin = open("27310.txt", "r")


q=input()

w=len(q)
for i in q:
    if i==':':
        w+=1
    if i=="_":
        w+=5
print(w)

import sys
sys.stdin = open("31822.txt", "r")


q=input()
s=int(input())
z=0
for _ in range(s):
    w=input()
    if w[:5]==q[:5]:
        z+=1
print(z)
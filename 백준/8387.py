import sys
sys.stdin = open("8387.txt", "r")

a=int(input())
b=input()
c=input()
s=0
for i in range(a):
    if b[i]==c[i]:
        s+=1
print(s)

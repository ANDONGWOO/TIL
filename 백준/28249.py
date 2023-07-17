import sys

sys.stdin = open("28249.txt", "r")

t=int(input())
s=0
for _ in range(t):
    q=input()
    if q=="Poblano":
        s+=1500
    elif q=="Mirasol":
        s+=6000
    elif q=="Serrano":
        s+=15500
    elif q=="Cayenne":
        s+=40000
    elif q=="Thai":
        s+=75000
    else:
        s+=125000
print(s)
import sys

sys.stdin = open("26545.txt", "r")

t=int(input())
s=0
for i in range(t):
    s+=int(input())
print(s)
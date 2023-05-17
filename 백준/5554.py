import sys
sys.stdin = open("5554.txt", "r")

s=0

for i in range(4):
    s+=int(input())
print(s//60)
print(s%60)
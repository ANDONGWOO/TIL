import sys
sys.stdin = open("5565.txt", "r")

s=int(input())
q=0
for i in range(9):
    q+=int(input())
print(s-q)
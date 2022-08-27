
import sys

sys.stdin = open("10039.txt", "r")
input=sys.stdin.readlines

a=list(map(lambda s: s.strip(), input()))
s=0
for i in range(len(a)):
    if int(a[i])<40:
        a[i]=40


print(int((int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4]))/5))

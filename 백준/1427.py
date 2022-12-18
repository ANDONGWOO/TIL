import sys

sys.stdin = open("1427.txt", "r")

a = input()
a = sorted(a)
a.sort(reverse=True)

print(*a,sep="")#sep="" 공백제거


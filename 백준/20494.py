import sys
sys.stdin = open("20494.txt", "r")


s=0

for i in range(int(input())):
    s+=len(input())
print(s)
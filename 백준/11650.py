import sys
sys.stdin = open("11650.txt", "r")

n = int(input())
a= []

for _ in range(n):
    x, y = map(int, input().split())
    a.append([x,y])
a.sort()

for i in a:
    print(i[0],i[1])
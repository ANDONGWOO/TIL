
import sys
sys.stdin = open("10814.txt", "r")
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(sys.stdin.readline().split()))
a.sort(key=lambda x: int (x[0]))
for i in range(n):
    print(a[i][0],a[i][1])

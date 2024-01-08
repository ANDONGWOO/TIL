import sys
sys.stdin = open("30999.txt", "r")
q, w = map(int, input().split())
e = [input().strip() for _ in range(q)]


s = 0

for i in range(q):
    x = e[i].count('O')
    m = w - x

    if x > m:
        s += 1
print(s)
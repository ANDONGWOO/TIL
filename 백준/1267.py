import sys
sys.stdin = open("1267.txt", "r")

n = int(input())
q = list(map(int, input().split()))
a = 0
b = 0
for i in q:
    a += i // 30 * 10 + 10
    b += i // 60 * 15 + 15
if a < b:
    print('Y %d' % a)
elif a > b:
    print('M %d' % b)
else:
    print('Y M %d' % a)
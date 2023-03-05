import sys
sys.stdin = open("5635.txt", "r")


q = []
t=int(input())
for _ in range(t):
    a,b,c,d = input().rstrip().split()
    b,c,d = map(int,(b,c,d))
    q.append((d,c,b,a))
q.sort()
print(q[-1][3])
print(q[0][3])
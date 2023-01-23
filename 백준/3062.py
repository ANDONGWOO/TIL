import sys
sys.stdin = open("3062.txt", "r")

for _ in range(int(input())):
    t=input()
    q=str(int(t) + int(t[::-1]))
    if q == q[::-1]:
        print('YES')
    else:
        print('NO')
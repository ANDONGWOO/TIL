import sys
sys.stdin = open("11945.txt", "r")

n,m = map(int, input().split())

for i in range(n):
    s=input()
    print(s[::-1])
#역순 출력
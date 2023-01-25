import sys
sys.stdin = open("11944.txt", "r")

n,m = map(int, input().split())

print((str(n)*n)[:m])


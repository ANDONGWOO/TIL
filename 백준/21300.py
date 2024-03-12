import sys
sys.stdin = open("21300.txt", "r")

q=list(map(int,input().split()))

print(sum(q)*5)
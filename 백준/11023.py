import sys
sys.stdin = open("11023.txt", "r")

n=list(map(int,input().split()))

print(sum(n))
import sys
sys.stdin = open("27866.txt", "r")

n=list(input())
q=int(input())
print(*n[q-1:q])
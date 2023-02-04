import sys
sys.stdin = open("1037.txt", "r")

q=int(input())
w=list(map(int,input().split()))
w.sort()
print(w[0]*w[-1])
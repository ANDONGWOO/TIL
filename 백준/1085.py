import sys
sys.stdin = open("1085.txt", "r")

a,b,c,d=map(int,input().split())

print(min(a,b,c-a,d-b))
import sys
sys.stdin = open("31428.txt", "r")

n=int(input())
q=list(map(str,input().split()))
w=input()

print(q.count(w))
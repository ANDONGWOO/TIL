import sys
sys.stdin = open("11728.txt", "r")

a,b = map(int, input().split())
q=list(map(int,input().split()))
w=list(map(int,input().split()))
e=[]
e=sorted(q+w)
print(*e)
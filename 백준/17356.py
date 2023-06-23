import sys
sys.stdin = open("17356.txt", "r")


a,b=map(float,input().split())


q=(b-a)/400
w=1/(1+10**q)
print(w)
import sys
sys.stdin = open("30822.txt", "r")

s=int(input())

q=input()

w=q.count('u'),q.count('o'),q.count('s'),q.count('p'),q.count('c')
print(min(w))
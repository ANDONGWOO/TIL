import sys
sys.stdin = open("18409.txt", "r")

q=int(input())
t=list(input())
s=0

s+=t.count('a')
s+=t.count('i')
s+=t.count('u')
s+=t.count('e')
s+=t.count('o')
print(s)

import sys
sys.stdin = open("10987.txt", "r")


q=input()
s=0

s+=q.count('a')
s+=q.count('e')
s+=q.count('i')
s+=q.count('o')
s+=q.count('u')

print(s)
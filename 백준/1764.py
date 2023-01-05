
import sys

sys.stdin = open("1764.txt", "r")

a,b= map(int,input().split())
q=set()
w=set()
for _ in range(a):
    q.add(input())
for _ in range(b):
    w.add(input())

e=sorted(list(q&w))#교집합
print(len(e))

for i in e:
    print(i)
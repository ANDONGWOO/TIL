import sys

sys.stdin = open("1919.txt", "r")

q=list(input())
w=list(input())
e,r=q[:],w[:]
a=[x for x in q if not x in r or r.remove(x)]
b=[x for x in w if not x in e or e.remove(x)]
print(len(a)+len(b))


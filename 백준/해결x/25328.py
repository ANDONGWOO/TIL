import sys
from itertools import combinations

sys.stdin = open("25328.txt", "r")

a=list(input())
b=list(input())
c=list(input())
d=int(input())

q=list(combinations(a,d))+list(combinations(b,d))+list(combinations(c,d))#조합 a,b,c 합하고

visited = set()
w = [x for x in q if x in visited or (visited.add(x) or False)]#중복 요소 추출

if len(w)>=1:
    for i in w:
        print(*i,sep="")
else:
    print(-1)

import sys
from itertools import combinations
sys.stdin = open("6603.txt", "r")


while 1:
    t=list(map(int,input().split()))
    w=t[1:]
    q=t[0]
    for i in combinations(w,6):#w리스트에서 6개 조합 중복 x
        print(*i)
    if q==0:
        break
    print()


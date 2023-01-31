import sys
import itertools
sys.stdin = open("3040.txt", "r")

t=[int(input()) for _ in range(9)]
for i in itertools.combinations(t,7):#itertools.combinations 조합 7개의 조합 중복x
    if sum(i)==100:
        for k in sorted(i):
            print(k)
        break
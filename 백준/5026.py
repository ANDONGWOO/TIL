import sys
sys.stdin = open("5026.txt", "r")

t=int(input())

for _ in range(t):
    q=input()
    if q=="P=NP":
        print('skipped')
        continue
    else:
        print(sum(map(int,q.split("+"))))
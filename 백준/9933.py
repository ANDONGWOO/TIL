import sys

sys.stdin = open("9933.txt", "r")

n=int(input())
q=[input() for _ in range(n)]
for i in q:
    if i[::-1] in q:
        break
z=len(i)//2#인덱스0시작
print(len(i),i[z])
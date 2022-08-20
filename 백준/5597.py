import sys

sys.stdin = open("5597.txt", "r")

q=[z for z in range(1,31)]
for i in range(1,29):
    q.remove(int(input()))
print(*q,sep='\n')
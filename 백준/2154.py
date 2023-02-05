import sys

sys.stdin = open("2154.txt", "r")

t=""

for i in range(1,100000+1):
    t+=str(i)
print(t.index(input())+1)

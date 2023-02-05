import sys
sys.stdin = open("8545.txt", "r")

s=input()

for i in reversed(s):
    print(i,end="")
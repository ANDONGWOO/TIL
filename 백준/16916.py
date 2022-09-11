import sys
sys.stdin = open("16916.txt", "r")

p=input()
s=input()

if s in p:#s가 p들어가면 1
    print(1)
else:#아니면 0
    print(0)
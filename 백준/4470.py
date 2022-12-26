import sys
sys.stdin = open("4470.txt", "r")

t=int(input())

for i in range(1,t+1):
    a=input()
    print(f"{i}. {(a)}")
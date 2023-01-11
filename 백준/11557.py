import sys

sys.stdin = open("11557.txt", "r")


for i in range(int(input())):
    c=[input().split() for _ in range(int(input()))]
    c.sort(key= lambda x:int(x[1]))
    print(c[-1][0])#마지막 학교의 이름

import sys
sys.stdin = open("4458.txt", "r")
c=int(input())

for i in range(c):
    t=input()
    print(t[0].upper()+t[1:])

#t[0] 소문자에서 대문자로 +t[1:]출력
import sys
sys.stdin = open("4740.txt", "r")

while 1:
    t=list(input())
    if t[0] == '*' and t[1] =='*' and t[2] == '*':
        break
    # print(*t[::-1], sep="")#t[::-1] 역순
    t.reverse()
    print(*t,sep="")# reverse 역순

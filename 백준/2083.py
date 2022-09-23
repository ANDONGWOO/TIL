import sys

sys.stdin = open("2083.txt", "r")
input=sys.stdin.readline

while 1:
    s=input().split()
    if s[0]=='#' and (s[1]=='0' and s[2]=='0'):#종료
        break
    elif int(s[1])>17 or int(s[2])>=80:#나이가 17보다 크거나 몸무게가 80이상면(성인부)
        print(s[0],'Senior')
    else:#청소년부
        print(s[0],'Junior')

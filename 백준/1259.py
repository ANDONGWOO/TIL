import sys

sys.stdin = open("1259.txt", "r")

while 1:
    t=input()
    if t=='0':#0이면 끝
        break
    if t==t[::-1]:#원래랑 뒤에서부터 읽어도 같다면
        print('yes')
    else:
        print("no")
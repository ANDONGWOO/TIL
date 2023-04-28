import sys
sys.stdin = open("27930.txt", "r")

s=list(input())

KOREA=["K" ,"O" ,"R" ,"E" ,"A"]
YONSEI=["Y" ,"O" ,"N" ,"S" ,"E" ,"I"]
for i in s:
    if i in KOREA:
        KOREA.remove(i)
        if len(KOREA)==0:
            print("KOREA")
            break
    if i in YONSEI:
        YONSEI.remove(i)
        if len(YONSEI)==0:
            print("YONSEI")
            break

import sys

sys.stdin = open("24883.txt", "r")
q=input()
if q=="n" or q=="N":#q가 n이나N 이면 "Naver D2"
    print("Naver D2")
else:
    print("Naver Whale") 
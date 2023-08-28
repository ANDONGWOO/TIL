import sys
sys.stdin = open("5073.txt", "r")

while 1:
    s=list(map(int,input().split()))
    s.sort()
    if s[0]==0 and s[1]==0 and s[2]==0:
        break
    if s[0]+s[1]<=s[2]:#조건x부터
        print("Invalid")
    elif s[0]==s[1] and s[1]==s[2]:
        print("Equilateral")
    elif s[0]==s[1] or s[1]==s[2] or s[0]==s[2]:
        print("Isosceles")
    else:
        print("Scalene")
import sys

sys.stdin = open("11365.txt", "r")

while 1 :
    q=input()
    if q=='END':
        break
    print(q[::-1])
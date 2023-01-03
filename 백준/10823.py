import sys

sys.stdin = open("10823.txt", "r")

s = ''
while 1:
    try:
        s += input()
    except:
        break
print(sum(map(int,s.split(','))))
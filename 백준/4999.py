import sys
sys.stdin = open("4999.txt", "r")

a=input()
b=input()

if len(a) >= len(b):
    print('go')
else:
    print('no')
import sys

sys.stdin = open("27328.txt", "r")

a=int(input())
b=int(input())
if a<b:
    print('-1')
elif a>b:
    print('1')
else:
    print('0')
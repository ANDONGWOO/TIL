
import sys

sys.stdin = open("2490.txt", "r")
input=sys.stdin.readlines

for i in list(map(lambda s: s.strip(), input())):
    q=i.count('0')
    if q==1:
        print('A')
    if q==2:
        print('B')
    if q==3:
        print('C')
    if q==4:
        print('D')
    if q==0:
        print('E')

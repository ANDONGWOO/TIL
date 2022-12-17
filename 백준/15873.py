import sys
sys.stdin = open("15873.txt", "r")

t=input()
if len(t)==2:#길이 2면
    print(int(t[0])+int(t[1]))
elif len(t)==3:
    if t[1] == '0':
        print(int(t[:2])+int(t[-1]))
    if t[-1]== "0":
        print(int(t[0])+int(t[1:3]))
elif len(t)==4:
    print(int(t[0:2])+int(t[2:4]))
 
import sys
sys.stdin = open("10768.txt", "r")

a=int(input())
b=int(input())


if a<2:
    print("Before")
elif a==2:
    if b<18:
        print("Before")
    elif b>18:
        print("After")
    else:
        print("Special")
else:
    print("After")
